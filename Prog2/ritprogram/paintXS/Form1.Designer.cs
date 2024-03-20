
namespace paintXS
{
    partial class FRMPaintProgram
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
            this.pbxPaintArea = new System.Windows.Forms.PictureBox();
            this.lblDebugText = new System.Windows.Forms.Label();
            this.tbSize = new System.Windows.Forms.TrackBar();
            this.colorDialog = new System.Windows.Forms.ColorDialog();
            this.pbColourSelection = new System.Windows.Forms.PictureBox();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            ((System.ComponentModel.ISupportInitialize)(this.pbxPaintArea)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbSize)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbColourSelection)).BeginInit();
            this.SuspendLayout();
            // 
            // pbxPaintArea
            // 
            this.pbxPaintArea.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pbxPaintArea.Location = new System.Drawing.Point(12, 129);
            this.pbxPaintArea.Name = "pbxPaintArea";
            this.pbxPaintArea.Size = new System.Drawing.Size(1197, 530);
            this.pbxPaintArea.TabIndex = 0;
            this.pbxPaintArea.TabStop = false;
            this.pbxPaintArea.Paint += new System.Windows.Forms.PaintEventHandler(this.pbxPaintArea_Paint);
            this.pbxPaintArea.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pbxPaintArea_MouseDown);
            this.pbxPaintArea.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pbxPaintArea_MouseMove);
            this.pbxPaintArea.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pbxPaintArea_MouseUp);
            // 
            // lblDebugText
            // 
            this.lblDebugText.AutoSize = true;
            this.lblDebugText.Location = new System.Drawing.Point(9, 9);
            this.lblDebugText.Name = "lblDebugText";
            this.lblDebugText.Size = new System.Drawing.Size(58, 13);
            this.lblDebugText.TabIndex = 1;
            this.lblDebugText.Text = "debugText";
            // 
            // tbSize
            // 
            this.tbSize.Location = new System.Drawing.Point(456, 23);
            this.tbSize.Maximum = 100;
            this.tbSize.Name = "tbSize";
            this.tbSize.Size = new System.Drawing.Size(228, 45);
            this.tbSize.SmallChange = 10;
            this.tbSize.TabIndex = 2;
            this.tbSize.Scroll += new System.EventHandler(this.tbSize_Scroll);
            // 
            // pbColourSelection
            // 
            this.pbColourSelection.BackColor = System.Drawing.Color.Black;
            this.pbColourSelection.Location = new System.Drawing.Point(730, 32);
            this.pbColourSelection.Name = "pbColourSelection";
            this.pbColourSelection.Size = new System.Drawing.Size(185, 36);
            this.pbColourSelection.TabIndex = 3;
            this.pbColourSelection.TabStop = false;
            this.pbColourSelection.Click += new System.EventHandler(this.pbColourSelection_Click);
            // 
            // FRMPaintProgram
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1221, 671);
            this.Controls.Add(this.pbColourSelection);
            this.Controls.Add(this.tbSize);
            this.Controls.Add(this.lblDebugText);
            this.Controls.Add(this.pbxPaintArea);
            this.Name = "FRMPaintProgram";
            this.Text = "paintXS";
            ((System.ComponentModel.ISupportInitialize)(this.pbxPaintArea)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbSize)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbColourSelection)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pbxPaintArea;
        private System.Windows.Forms.Label lblDebugText;
        private System.Windows.Forms.TrackBar tbSize;
        private System.Windows.Forms.ColorDialog colorDialog;
        private System.Windows.Forms.PictureBox pbColourSelection;
        private System.Windows.Forms.ColorDialog colorDialog1;
    }
}

