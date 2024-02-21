
namespace WindowsFormsApp1
{
    partial class Form1
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
            this.tbxTal = new System.Windows.Forms.TextBox();
            this.lblTal = new System.Windows.Forms.Label();
            this.lblKvadrat = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // tbxTal
            // 
            this.tbxTal.Location = new System.Drawing.Point(165, 56);
            this.tbxTal.Name = "tbxTal";
            this.tbxTal.Size = new System.Drawing.Size(100, 20);
            this.tbxTal.TabIndex = 0;
            // 
            // lblTal
            // 
            this.lblTal.AutoSize = true;
            this.lblTal.Location = new System.Drawing.Point(84, 59);
            this.lblTal.Name = "lblTal";
            this.lblTal.Size = new System.Drawing.Size(25, 13);
            this.lblTal.TabIndex = 1;
            this.lblTal.Text = "Tal:";
            // 
            // lblKvadrat
            // 
            this.lblKvadrat.AutoSize = true;
            this.lblKvadrat.Location = new System.Drawing.Point(162, 153);
            this.lblKvadrat.Name = "lblKvadrat";
            this.lblKvadrat.Size = new System.Drawing.Size(0, 13);
            this.lblKvadrat.TabIndex = 2;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(120, 228);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(145, 50);
            this.button1.TabIndex = 3;
            this.button1.Text = "Beräkna Kvadraten";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(406, 346);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.lblKvadrat);
            this.Controls.Add(this.lblTal);
            this.Controls.Add(this.tbxTal);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbxTal;
        private System.Windows.Forms.Label lblTal;
        private System.Windows.Forms.Label lblKvadrat;
        private System.Windows.Forms.Button button1;
    }
}

