
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
            this.tbxTal1 = new System.Windows.Forms.TextBox();
            this.lblTal = new System.Windows.Forms.Label();
            this.btnSumma = new System.Windows.Forms.Button();
            this.tbxTal2 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.lblSum = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // tbxTal1
            // 
            this.tbxTal1.Location = new System.Drawing.Point(147, 81);
            this.tbxTal1.Name = "tbxTal1";
            this.tbxTal1.Size = new System.Drawing.Size(100, 20);
            this.tbxTal1.TabIndex = 0;
            // 
            // lblTal
            // 
            this.lblTal.AutoSize = true;
            this.lblTal.Location = new System.Drawing.Point(96, 81);
            this.lblTal.Name = "lblTal";
            this.lblTal.Size = new System.Drawing.Size(34, 13);
            this.lblTal.TabIndex = 1;
            this.lblTal.Text = "Tal 1:";
            // 
            // btnSumma
            // 
            this.btnSumma.Location = new System.Drawing.Point(120, 228);
            this.btnSumma.Name = "btnSumma";
            this.btnSumma.Size = new System.Drawing.Size(145, 50);
            this.btnSumma.TabIndex = 3;
            this.btnSumma.Text = "Beräkna Summan";
            this.btnSumma.UseVisualStyleBackColor = true;
            this.btnSumma.Click += new System.EventHandler(this.button1_Click);
            // 
            // tbxTal2
            // 
            this.tbxTal2.Location = new System.Drawing.Point(147, 119);
            this.tbxTal2.Name = "tbxTal2";
            this.tbxTal2.Size = new System.Drawing.Size(100, 20);
            this.tbxTal2.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(96, 122);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(34, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "Tal 2:";
            // 
            // lblSum
            // 
            this.lblSum.AutoSize = true;
            this.lblSum.Location = new System.Drawing.Point(117, 185);
            this.lblSum.Name = "lblSum";
            this.lblSum.Size = new System.Drawing.Size(0, 13);
            this.lblSum.TabIndex = 6;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(406, 346);
            this.Controls.Add(this.lblSum);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tbxTal2);
            this.Controls.Add(this.btnSumma);
            this.Controls.Add(this.lblTal);
            this.Controls.Add(this.tbxTal1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbxTal1;
        private System.Windows.Forms.Label lblTal;
        private System.Windows.Forms.Button btnSumma;
        private System.Windows.Forms.TextBox tbxTal2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblSum;
    }
}

