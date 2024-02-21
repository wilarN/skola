
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
            this.label2 = new System.Windows.Forms.Label();
            this.tbxTal3 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // tbxTal1
            // 
            this.tbxTal1.Location = new System.Drawing.Point(196, 100);
            this.tbxTal1.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.tbxTal1.Name = "tbxTal1";
            this.tbxTal1.Size = new System.Drawing.Size(132, 22);
            this.tbxTal1.TabIndex = 0;
            // 
            // lblTal
            // 
            this.lblTal.AutoSize = true;
            this.lblTal.Location = new System.Drawing.Point(128, 100);
            this.lblTal.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblTal.Name = "lblTal";
            this.lblTal.Size = new System.Drawing.Size(41, 16);
            this.lblTal.TabIndex = 1;
            this.lblTal.Text = "Tal 1:";
            // 
            // btnSumma
            // 
            this.btnSumma.Location = new System.Drawing.Point(160, 281);
            this.btnSumma.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.btnSumma.Name = "btnSumma";
            this.btnSumma.Size = new System.Drawing.Size(193, 62);
            this.btnSumma.TabIndex = 3;
            this.btnSumma.Text = "Beräkna Medelvärde";
            this.btnSumma.UseVisualStyleBackColor = true;
            this.btnSumma.Click += new System.EventHandler(this.button1_Click);
            // 
            // tbxTal2
            // 
            this.tbxTal2.Location = new System.Drawing.Point(196, 146);
            this.tbxTal2.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.tbxTal2.Name = "tbxTal2";
            this.tbxTal2.Size = new System.Drawing.Size(132, 22);
            this.tbxTal2.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(128, 150);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 16);
            this.label1.TabIndex = 5;
            this.label1.Text = "Tal 2:";
            // 
            // lblSum
            // 
            this.lblSum.AutoSize = true;
            this.lblSum.Location = new System.Drawing.Point(157, 233);
            this.lblSum.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblSum.Name = "lblSum";
            this.lblSum.Size = new System.Drawing.Size(0, 16);
            this.lblSum.TabIndex = 6;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(128, 194);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(41, 16);
            this.label2.TabIndex = 8;
            this.label2.Text = "Tal 3:";
            // 
            // tbxTal3
            // 
            this.tbxTal3.Location = new System.Drawing.Point(196, 187);
            this.tbxTal3.Name = "tbxTal3";
            this.tbxTal3.Size = new System.Drawing.Size(132, 22);
            this.tbxTal3.TabIndex = 9;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(541, 426);
            this.Controls.Add(this.tbxTal3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.lblSum);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tbxTal2);
            this.Controls.Add(this.btnSumma);
            this.Controls.Add(this.lblTal);
            this.Controls.Add(this.tbxTal1);
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
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
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tbxTal3;
    }
}

