﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace tcpCommunication
{
    public partial class login : Form
    {
        public login()
        {
            InitializeComponent();
        }

        private void btnConnectFromLogin_Click(object sender, EventArgs e)
        {
            string username = tbxLoginUsrnm.Text;

            if (username != "")
            {
                client client = new client(username);
                client.Show();
                this.Hide();
            }
            else
            {
                MessageBox.Show("Please enter a username");
            }
        }
    }
}
