
namespace GFÖ
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
            this.tbxRadius = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.lblMultiplier = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // tbxRadius
            // 
            this.tbxRadius.Location = new System.Drawing.Point(379, 47);
            this.tbxRadius.Name = "tbxRadius";
            this.tbxRadius.Size = new System.Drawing.Size(114, 20);
            this.tbxRadius.TabIndex = 0;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(499, 24);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(105, 65);
            this.button1.TabIndex = 1;
            this.button1.Text = "Update Radius Modifier";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // lblMultiplier
            // 
            this.lblMultiplier.AutoSize = true;
            this.lblMultiplier.Location = new System.Drawing.Point(248, 50);
            this.lblMultiplier.Name = "lblMultiplier";
            this.lblMultiplier.Size = new System.Drawing.Size(125, 15);
            this.lblMultiplier.TabIndex = 2;
            this.lblMultiplier.Text = "Multiplier (int/float) =>";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(982, 453);
            this.Controls.Add(this.lblMultiplier);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.tbxRadius);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox tbxRadius;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label lblMultiplier;
    }
}

