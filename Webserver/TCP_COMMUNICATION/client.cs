using System;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;

namespace tcpCommunication
{
    public partial class client : Form
    {
        // Set the port number
        static int PORT = 24456;

        // Create a TcpClient object
        TcpClient comClient;

        // Create a string to store the username further down, when the login form has been passed.
        string username;

        public client(string username)
        {

            // Set the username gotten from the login form
            this.username = username;
            InitializeComponent();
        }

        private async void btnConn_Click(object sender, EventArgs e)
        {
            try
            {
                IPAddress IPADDR = IPAddress.Parse(tbxIP.Text);
                comClient = new TcpClient();
                comClient.NoDelay = true;
                await comClient.ConnectAsync(IPADDR, PORT);

                // Send username to server
                byte[] sendData = Encoding.Unicode.GetBytes(username);
                await comClient.GetStream().WriteAsync(sendData, 0, sendData.Length);

                MessageBox.Show("Connected to server");
                tbxChatRoom.Text += "Connected to server ["+ comClient.Client.RemoteEndPoint + "]\r\n";

                // Hide the IP textbox and button
                tbxIP.Visible = false;
                label1.Visible = false;
                btnConn.Visible = false;
                btnSend.Visible = false;

                // Show the chatroom and message box
                tbxChatRoom.Visible = true;
                tbxMessageMain.Visible = true;
                btnSend.Visible = true;


                // Start listening for messages from server asynchronously
                _ = Task.Run(() => ListenForMessages());
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private async void btnSend_Click(object sender, EventArgs e)
        {
            // Send message to server
            try
            {
                if (comClient == null || !comClient.Connected)
                {
                    MessageBox.Show("Not connected to server");
                    return;
                }

                byte[] sendData = Encoding.Unicode.GetBytes(username + " --> " + tbxMessageMain.Text);
                await comClient.GetStream().WriteAsync(sendData, 0, sendData.Length);

                // Clear the message box
                tbxMessageMain.Clear();

            }
            catch (Exception err)
            {
                // Display error message
                MessageBox.Show(err.Message, Text);
            }
        }

        private async Task ListenForMessages()
        {
            // Listen for messages from the server
            try
            {
                NetworkStream stream = comClient.GetStream();
                byte[] buffer = new byte[1024];

                while (true)
                {
                    int bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length);
                    if (bytesRead == 0)
                    {
                        break; // Connection closed
                    }

                    // Convert the message to a string
                    string message = Encoding.Unicode.GetString(buffer, 0, bytesRead);

                    // Display the message in the chatroom textbox
                    Invoke(new Action(() => tbxChatRoom.Text += message + "\r\n"));

                    // Scroll to the bottom of the chatroom textbox
                    Invoke(new Action(() => tbxChatRoom.SelectionStart = tbxChatRoom.Text.Length));
                    Invoke(new Action(() => tbxChatRoom.ScrollToCaret()));

                }
            }
            catch (Exception ex)
            {
                // Display error message
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void client_Load(object sender, EventArgs e)
        {
            // Display the username in the form
            lblWelcome.Text = "Welcome, " + username + "!";

            // Show logged in as
            lblLoggedInAs.Text = "Logged in as: " + username;

            // Hide chatroom and message box
            tbxChatRoom.Visible = false;
            tbxMessageMain.Visible = false;
        }

        private async void btnLogout_Click(object sender, EventArgs e)
        {
            // Logout and close the form.

            // Send logout message to server
            byte[] sendData = Encoding.Unicode.GetBytes(username + " has logged out.");
            await comClient.GetStream().WriteAsync(sendData, 0, sendData.Length);

            MessageBox.Show("Logged out");
            this.Close();
        }

        private void tbxMessageMain_KeyDown(object sender, KeyEventArgs e)
        {
            // Send message when enter key is pressed
            if (e.KeyCode == Keys.Enter)
            {
                btnSend.PerformClick();
            }
        }
    }
}
