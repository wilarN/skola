using System;
using System.Net.Sockets;
using System.Text;
using System.Windows.Forms;
using System.Net;

namespace tcpCommunication
{
    public partial class client : Form
    {
        static int PORT = 24456;
        TcpClient comClient;
        string username;

        public client()
        {
            InitializeComponent();
        }

        private void btnConn_Click(object sender, EventArgs e)
        {
            try
            {
                IPAddress IPADDR = IPAddress.Parse(tbxIP.Text);
                comClient = new TcpClient();
                comClient.NoDelay = true;
                comClient.Connect(IPADDR, PORT);

            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void btnSend_Click(object sender, EventArgs e)
        {
            try
            {
                if(tbxUsername.Text.Length < 1)
                {
                    // Empty username.
                    username = "Anonymous user";
                }
                else
                {
                    username = tbxUsername.Text;
                }

                if (comClient.Connected)
                {
                    byte[] sendData = Encoding.Unicode.GetBytes(username + " --> " + tbxMessageMain.Text);

                    comClient.GetStream().Write(sendData, 0, sendData.Length);

                    // You may want to wait for acknowledgment from the server before closing the connection.
                    // comClient.Close();
                }

            }catch(Exception err)
            {
                MessageBox.Show(err.Message, Text);
            }
        }
    }
}
