
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
            this.rbPen = new System.Windows.Forms.RadioButton();
            this.rbRect = new System.Windows.Forms.RadioButton();
            this.gbxRadio = new System.Windows.Forms.GroupBox();
            this.btnClear = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pbxPaintArea)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbSize)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbColourSelection)).BeginInit();
            this.gbxRadio.SuspendLayout();
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
            this.tbSize.SmallChange = 30;
            this.tbSize.TabIndex = 10;
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
            // rbPen
            // 
            this.rbPen.AutoSize = true;
            this.rbPen.Location = new System.Drawing.Point(21, 20);
            this.rbPen.Name = "rbPen";
            this.rbPen.Size = new System.Drawing.Size(56, 17);
            this.rbPen.TabIndex = 11;
            this.rbPen.TabStop = true;
            this.rbPen.Text = "Penna";
            this.rbPen.UseVisualStyleBackColor = true;
            // 
            // rbRect
            // 
            this.rbRect.AutoSize = true;
            this.rbRect.Location = new System.Drawing.Point(21, 43);
            this.rbRect.Name = "rbRect";
            this.rbRect.Size = new System.Drawing.Size(74, 17);
            this.rbRect.TabIndex = 12;
            this.rbRect.TabStop = true;
            this.rbRect.Text = "Rektangel";
            this.rbRect.UseVisualStyleBackColor = true;
            // 
            // gbxRadio
            // 
            this.gbxRadio.Controls.Add(this.rbPen);
            this.gbxRadio.Controls.Add(this.rbRect);
            this.gbxRadio.Location = new System.Drawing.Point(24, 23);
            this.gbxRadio.Name = "gbxRadio";
            this.gbxRadio.Size = new System.Drawing.Size(373, 89);
            this.gbxRadio.TabIndex = 13;
            this.gbxRadio.TabStop = false;
            this.gbxRadio.Text = "Verktyg";
            // 
            // btnClear
            // 
            this.btnClear.Location = new System.Drawing.Point(1110, 44);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(75, 68);
            this.btnClear.TabIndex = 14;
            this.btnClear.Text = "Rensa";
            this.btnClear.UseVisualStyleBackColor = true;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // FRMPaintProgram
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1221, 671);
            this.Controls.Add(this.btnClear);
            this.Controls.Add(this.gbxRadio);
            this.Controls.Add(this.pbColourSelection);
            this.Controls.Add(this.tbSize);
            this.Controls.Add(this.lblDebugText);
            this.Controls.Add(this.pbxPaintArea);
            this.Name = "FRMPaintProgram";
            this.Text = "paintXS";
            ((System.ComponentModel.ISupportInitialize)(this.pbxPaintArea)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbSize)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbColourSelection)).EndInit();
            this.gbxRadio.ResumeLayout(false);
            this.gbxRadio.PerformLayout();
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
        private System.Windows.Forms.RadioButton rbPen;
        private System.Windows.Forms.RadioButton rbRect;
        private System.Windows.Forms.GroupBox gbxRadio;
        private System.Windows.Forms.Button btnClear;
    }
}

