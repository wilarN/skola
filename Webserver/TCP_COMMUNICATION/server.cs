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

        public server()
        {
            InitializeComponent();
        }

        private async void btnStartServer_Click(object sender, EventArgs e)
        {
            try
            {
                LISTENER = new TcpListener(IPAddress.Any, PORT);
                LISTENER.Start();

                while (true)
                {
                    TcpClient CLIENT = await LISTENER.AcceptTcpClientAsync();
                    activeConnections.Add(CLIENT);
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

                    tbxInbox.AppendText(receivedMessage.TrimStart());
                    tbxInbox.AppendText(Environment.NewLine);
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
