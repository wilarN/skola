
namespace tcpCommunication
{
    partial class client
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.tbxIP = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnConn = new System.Windows.Forms.Button();
            this.btnSend = new System.Windows.Forms.Button();
            this.tbxMessageMain = new System.Windows.Forms.TextBox();
            this.lblWelcome = new System.Windows.Forms.Label();
            this.lblLoggedInAs = new System.Windows.Forms.Label();
            this.btnLogout = new System.Windows.Forms.Button();
            this.tbxChatRoom = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // tbxIP
            // 
            this.tbxIP.Location = new System.Drawing.Point(266, 115);
            this.tbxIP.Name = "tbxIP";
            this.tbxIP.Size = new System.Drawing.Size(100, 20);
            this.tbxIP.TabIndex = 0;
            this.tbxIP.Text = "127.0.0.1";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(188, 118);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(54, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Server IP:";
            // 
            // btnConn
            // 
            this.btnConn.Location = new System.Drawing.Point(384, 112);
            this.btnConn.Name = "btnConn";
            this.btnConn.Size = new System.Drawing.Size(75, 23);
            this.btnConn.TabIndex = 3;
            this.btnConn.Text = "Connect";
            this.btnConn.UseVisualStyleBackColor = true;
            this.btnConn.Click += new System.EventHandler(this.btnConn_Click);
            // 
            // btnSend
            // 
            this.btnSend.Location = new System.Drawing.Point(449, 277);
            this.btnSend.Name = "btnSend";
            this.btnSend.Size = new System.Drawing.Size(120, 24);
            this.btnSend.TabIndex = 5;
            this.btnSend.Text = "Send";
            this.btnSend.UseVisualStyleBackColor = true;
            this.btnSend.Click += new System.EventHandler(this.btnSend_Click);
            // 
            // tbxMessageMain
            // 
            this.tbxMessageMain.Location = new System.Drawing.Point(148, 277);
            this.tbxMessageMain.Multiline = true;
            this.tbxMessageMain.Name = "tbxMessageMain";
            this.tbxMessageMain.Size = new System.Drawing.Size(295, 22);
            this.tbxMessageMain.TabIndex = 6;
            this.tbxMessageMain.KeyDown += new System.Windows.Forms.KeyEventHandler(this.tbxMessageMain_KeyDown);
            // 
            // lblWelcome
            // 
            this.lblWelcome.AutoSize = true;
            this.lblWelcome.BackColor = System.Drawing.Color.Transparent;
            this.lblWelcome.Font = new System.Drawing.Font("Microsoft Sans Serif", 30F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblWelcome.ForeColor = System.Drawing.SystemColors.Control;
            this.lblWelcome.Location = new System.Drawing.Point(183, 26);
            this.lblWelcome.Name = "lblWelcome";
            this.lblWelcome.Size = new System.Drawing.Size(422, 46);
            this.lblWelcome.TabIndex = 7;
            this.lblWelcome.Text = "Welcome Placeholder!";
            // 
            // lblLoggedInAs
            // 
            this.lblLoggedInAs.AutoSize = true;
            this.lblLoggedInAs.BackColor = System.Drawing.Color.Transparent;
            this.lblLoggedInAs.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.lblLoggedInAs.Location = new System.Drawing.Point(24, 367);
            this.lblLoggedInAs.Name = "lblLoggedInAs";
            this.lblLoggedInAs.Size = new System.Drawing.Size(129, 13);
            this.lblLoggedInAs.TabIndex = 8;
            this.lblLoggedInAs.Text = "Logged in as placeholder.";
            // 
            // btnLogout
            // 
            this.btnLogout.Location = new System.Drawing.Point(537, 353);
            this.btnLogout.Name = "btnLogout";
            this.btnLogout.Size = new System.Drawing.Size(148, 34);
            this.btnLogout.TabIndex = 9;
            this.btnLogout.Text = "Logout";
            this.btnLogout.UseVisualStyleBackColor = true;
            this.btnLogout.Click += new System.EventHandler(this.btnLogout_Click);
            // 
            // tbxChatRoom
            // 
            this.tbxChatRoom.Location = new System.Drawing.Point(148, 163);
            this.tbxChatRoom.Multiline = true;
            this.tbxChatRoom.Name = "tbxChatRoom";
            this.tbxChatRoom.Size = new System.Drawing.Size(421, 108);
            this.tbxChatRoom.TabIndex = 10;
            // 
            // client
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::tcpCommunication.Properties.Resources.warcraft_3_reforged_4k_2y_2048x1152_1071188565;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(697, 399);
            this.Controls.Add(this.tbxChatRoom);
            this.Controls.Add(this.btnLogout);
            this.Controls.Add(this.lblLoggedInAs);
            this.Controls.Add(this.lblWelcome);
            this.Controls.Add(this.tbxMessageMain);
            this.Controls.Add(this.btnSend);
            this.Controls.Add(this.btnConn);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tbxIP);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "client";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.Text = "client";
            this.Load += new System.EventHandler(this.client_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbxIP;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnConn;
        private System.Windows.Forms.Button btnSend;
        private System.Windows.Forms.TextBox tbxMessageMain;
        private System.Windows.Forms.Label lblWelcome;
        private System.Windows.Forms.Label lblLoggedInAs;
        private System.Windows.Forms.Button btnLogout;
        private System.Windows.Forms.TextBox tbxChatRoom;
    }
}