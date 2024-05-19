
namespace tcpCommunication
{
    partial class server
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
            this.tbxInbox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnStartServer = new System.Windows.Forms.Button();
            this.tbxUsers = new System.Windows.Forms.TextBox();
            this.lblUsers = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // tbxInbox
            // 
            this.tbxInbox.Location = new System.Drawing.Point(54, 208);
            this.tbxInbox.Multiline = true;
            this.tbxInbox.Name = "tbxInbox";
            this.tbxInbox.Size = new System.Drawing.Size(512, 128);
            this.tbxInbox.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(51, 192);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(43, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Chatlog";
            // 
            // btnStartServer
            // 
            this.btnStartServer.Location = new System.Drawing.Point(29, 65);
            this.btnStartServer.Name = "btnStartServer";
            this.btnStartServer.Size = new System.Drawing.Size(168, 61);
            this.btnStartServer.TabIndex = 2;
            this.btnStartServer.Text = "Start TCP Server";
            this.btnStartServer.UseVisualStyleBackColor = true;
            this.btnStartServer.Click += new System.EventHandler(this.btnStartServer_Click);
            // 
            // tbxUsers
            // 
            this.tbxUsers.Location = new System.Drawing.Point(277, 46);
            this.tbxUsers.Multiline = true;
            this.tbxUsers.Name = "tbxUsers";
            this.tbxUsers.Size = new System.Drawing.Size(289, 133);
            this.tbxUsers.TabIndex = 3;
            // 
            // lblUsers
            // 
            this.lblUsers.AutoSize = true;
            this.lblUsers.Location = new System.Drawing.Point(274, 30);
            this.lblUsers.Name = "lblUsers";
            this.lblUsers.Size = new System.Drawing.Size(77, 13);
            this.lblUsers.TabIndex = 4;
            this.lblUsers.Text = "Current clients:";
            // 
            // server
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::tcpCommunication.Properties.Resources._1083094_download_free_world_of_warcraft_backgrounds_3840x2160_1049736965;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(607, 348);
            this.Controls.Add(this.lblUsers);
            this.Controls.Add(this.tbxUsers);
            this.Controls.Add(this.btnStartServer);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tbxInbox);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "server";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "meltraTCP";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbxInbox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnStartServer;
        private System.Windows.Forms.TextBox tbxUsers;
        private System.Windows.Forms.Label lblUsers;
    }
}

