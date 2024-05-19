
namespace tcpCommunication
{
    partial class login
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
            this.tbxLoginUsrnm = new System.Windows.Forms.TextBox();
            this.lblUsername = new System.Windows.Forms.Label();
            this.btnConnectFromLogin = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // tbxLoginUsrnm
            // 
            this.tbxLoginUsrnm.Location = new System.Drawing.Point(280, 181);
            this.tbxLoginUsrnm.Name = "tbxLoginUsrnm";
            this.tbxLoginUsrnm.Size = new System.Drawing.Size(100, 20);
            this.tbxLoginUsrnm.TabIndex = 1;
            // 
            // lblUsername
            // 
            this.lblUsername.AutoSize = true;
            this.lblUsername.BackColor = System.Drawing.Color.WhiteSmoke;
            this.lblUsername.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lblUsername.Location = new System.Drawing.Point(216, 181);
            this.lblUsername.Name = "lblUsername";
            this.lblUsername.Size = new System.Drawing.Size(58, 13);
            this.lblUsername.TabIndex = 4;
            this.lblUsername.Text = "Username:";
            // 
            // btnConnectFromLogin
            // 
            this.btnConnectFromLogin.Location = new System.Drawing.Point(241, 224);
            this.btnConnectFromLogin.Name = "btnConnectFromLogin";
            this.btnConnectFromLogin.Size = new System.Drawing.Size(156, 46);
            this.btnConnectFromLogin.TabIndex = 5;
            this.btnConnectFromLogin.Text = "Login";
            this.btnConnectFromLogin.UseVisualStyleBackColor = true;
            this.btnConnectFromLogin.Click += new System.EventHandler(this.btnConnectFromLogin_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox1.BackgroundImage = global::tcpCommunication.Properties.Resources.world_of_warcraft__wotlk_logo_cut_down_by_death_gfx_d5patlq_28198843661;
            this.pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pictureBox1.Location = new System.Drawing.Point(140, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(380, 145);
            this.pictureBox1.TabIndex = 6;
            this.pictureBox1.TabStop = false;
            // 
            // login
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Black;
            this.BackgroundImage = global::tcpCommunication.Properties.Resources._792451_world_of_warcraft_wallpapers_2880x1800_for_mac_37949456;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(658, 365);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.btnConnectFromLogin);
            this.Controls.Add(this.lblUsername);
            this.Controls.Add(this.tbxLoginUsrnm);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "login";
            this.ShowIcon = false;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Login";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.TextBox tbxLoginUsrnm;
        private System.Windows.Forms.Label lblUsername;
        private System.Windows.Forms.Button btnConnectFromLogin;
        private System.Windows.Forms.PictureBox pictureBox1;
    }
}