using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using System.Collections.Generic;

namespace tcpCommunication
{
    public partial class server : Form
    {
        List<TcpClient> activeConnections = new List<TcpClient>();

        TcpListener LISTENER;
        int PORT = 24456;

        bool serverRunning = false;

        public server()
        {
            InitializeComponent();
        }

        private async void btnStartServer_Click(object sender, EventArgs e)
        {
            if (serverRunning)
            {
                // Stop server, if running
                try
                {
                    // Stop server
                    LISTENER.Stop();

                    // Close all active connections
                    foreach (TcpClient client in activeConnections)
                    {
                        client.Close();
                    }

                    serverRunning = false;
                    MessageBox.Show("Server stopped");
                    // Set label to show server is stopped
                    btnStartServer.Text = "Start TCP Server";
                    return;
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error stopping server: " + ex.Message);
                }
            }
            

            try
            {
                // Start server
                LISTENER = new TcpListener(IPAddress.Any, PORT);
                LISTENER.Start();

                MessageBox.Show("Server started on port: " + PORT);
                // Set label to show server is running
                btnStartServer.Text = "Stop TCP Server";
                serverRunning = true;

                // Show startup message in tbxInbox
                tbxInbox.AppendText("Server started on port: " + PORT);
                tbxInbox.AppendText(Environment.NewLine);

                // Start listening for clients
                while (true)
                {
                    if(!serverRunning)
                    {
                        break;
                    }
                    TcpClient CLIENT = await LISTENER.AcceptTcpClientAsync();
                    activeConnections.Add(CLIENT);
                    // Add client to list of active connections

                    // First message from client is username
                    byte[] recvData = new byte[1024];
                    int bytes = await CLIENT.GetStream().ReadAsync(recvData, 0, recvData.Length);
                    string receivedMessage = Encoding.Unicode.GetString(recvData, 0, bytes);

                    tbxUsers.AppendText( receivedMessage + "-->" + CLIENT.Client.RemoteEndPoint.ToString());

                    // New line
                    tbxUsers.AppendText(Environment.NewLine);

                    // Send connect message to all clients
                    foreach (TcpClient c in activeConnections)
                    {
                        byte[] sendData = Encoding.Unicode.GetBytes(receivedMessage + " has connected.");
                        await c.GetStream().WriteAsync(sendData, 0, sendData.Length);
                    }

                    // And in tbxInbox
                    tbxInbox.AppendText(receivedMessage + " has connected.");
                    tbxInbox.AppendText(Environment.NewLine);


                    HandleClient(CLIENT);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private async void HandleClient(TcpClient client)
        {
            try
            {

                // Send welcome message to client
                byte[] welcomeMessage = Encoding.Unicode.GetBytes("\r\nWelcome to the chat server!");
                await client.GetStream().WriteAsync(welcomeMessage, 0, welcomeMessage.Length);


                // Start listening for messages from handled client
                while (true)
                {

                    byte[] recvData = new byte[1024];
                    int bytes = await client.GetStream().ReadAsync(recvData, 0, recvData.Length);
                    if(bytes == 0)
                    {
                        activeConnections.Remove(client);
                        break;
                    }

                    string receivedMessage = Encoding.Unicode.GetString(recvData, 0, bytes);

                    // Handle logout message
                    if (receivedMessage.Contains("has logged out."))
                    {

                        // Get text before " has logged out."
                        receivedMessage = receivedMessage.Substring(0, receivedMessage.IndexOf(" has logged out."));

                        activeConnections.Remove(client);
                        // Remove client from textbox and --> ip in question
                        tbxUsers.Text = tbxUsers.Text.Replace(receivedMessage + "-->" + client.Client.RemoteEndPoint.ToString(), "");

                        client.Close();
                        break;
                    }

                    // Send message to all clients
                    foreach (TcpClient c in activeConnections)
                    {
                        //// Don't send message to sender
                        //if (c == client)
                        //{
                        //    continue;
                        //}

                        byte[] sendData = Encoding.Unicode.GetBytes(receivedMessage);
                        await c.GetStream().WriteAsync(sendData, 0, sendData.Length);
                    }

                    tbxInbox.AppendText(receivedMessage.TrimStart());
                    tbxInbox.AppendText(Environment.NewLine);

                    // Scroll to the bottom of the chatroom textbox
                    tbxInbox.SelectionStart = tbxInbox.Text.Length;
                    tbxInbox.ScrollToCaret();

                    Thread.Sleep(100);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }
    }
}
