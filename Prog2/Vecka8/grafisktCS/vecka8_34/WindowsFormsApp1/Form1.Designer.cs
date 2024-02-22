
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
            this.tbxText1 = new System.Windows.Forms.TextBox();
            this.lblTal = new System.Windows.Forms.Label();
            this.btnSumma = new System.Windows.Forms.Button();
            this.tbxText2 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.lblSum = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // tbxText1
            // 
            this.tbxText1.Location = new System.Drawing.Point(196, 100);
            this.tbxText1.Margin = new System.Windows.Forms.Padding(4);
            this.tbxText1.Name = "tbxText1";
            this.tbxText1.Size = new System.Drawing.Size(132, 22);
            this.tbxText1.TabIndex = 0;
            // 
            // lblTal
            // 
            this.lblTal.AutoSize = true;
            this.lblTal.Location = new System.Drawing.Point(58, 103);
            this.lblTal.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblTal.Name = "lblTal";
            this.lblTal.Size = new System.Drawing.Size(114, 17);
            this.lblTal.TabIndex = 1;
            this.lblTal.Text = "Första Textbiten:";
            // 
            // btnSumma
            // 
            this.btnSumma.Location = new System.Drawing.Point(160, 281);
            this.btnSumma.Margin = new System.Windows.Forms.Padding(4);
            this.btnSumma.Name = "btnSumma";
            this.btnSumma.Size = new System.Drawing.Size(193, 62);
            this.btnSumma.TabIndex = 3;
            this.btnSumma.Text = "Kombinera Textbitar";
            this.btnSumma.UseVisualStyleBackColor = true;
            this.btnSumma.Click += new System.EventHandler(this.button1_Click);
            // 
            // tbxText2
            // 
            this.tbxText2.Location = new System.Drawing.Point(196, 146);
            this.tbxText2.Margin = new System.Windows.Forms.Padding(4);
            this.tbxText2.Name = "tbxText2";
            this.tbxText2.Size = new System.Drawing.Size(132, 22);
            this.tbxText2.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(58, 149);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(112, 17);
            this.label1.TabIndex = 5;
            this.label1.Text = "Andra Textbiten:";
            // 
            // lblSum
            // 
            this.lblSum.AutoSize = true;
            this.lblSum.Location = new System.Drawing.Point(157, 233);
            this.lblSum.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblSum.Name = "lblSum";
            this.lblSum.Size = new System.Drawing.Size(0, 17);
            this.lblSum.TabIndex = 6;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(541, 426);
            this.Controls.Add(this.lblSum);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.tbxText2);
            this.Controls.Add(this.btnSumma);
            this.Controls.Add(this.lblTal);
            this.Controls.Add(this.tbxText1);
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbxText1;
        private System.Windows.Forms.Label lblTal;
        private System.Windows.Forms.Button btnSumma;
        private System.Windows.Forms.TextBox tbxText2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblSum;
    }
}

