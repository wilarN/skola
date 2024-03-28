
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
            this.tbSize = new System.Windows.Forms.TrackBar();
            this.colorDialog = new System.Windows.Forms.ColorDialog();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.gbxRadio = new System.Windows.Forms.GroupBox();
            this.pbxToolEraser = new System.Windows.Forms.PictureBox();
            this.pbxToolLine = new System.Windows.Forms.PictureBox();
            this.pbxToolSquare = new System.Windows.Forms.PictureBox();
            this.pbxToolPen = new System.Windows.Forms.PictureBox();
            this.pbxTrash = new System.Windows.Forms.PictureBox();
            this.pbColourSelection = new System.Windows.Forms.PictureBox();
            this.pbxPaintArea = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.tbSize)).BeginInit();
            this.gbxRadio.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolEraser)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolLine)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolSquare)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolPen)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxTrash)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbColourSelection)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxPaintArea)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // tbSize
            // 
            this.tbSize.Location = new System.Drawing.Point(476, 42);
            this.tbSize.Maximum = 100;
            this.tbSize.Name = "tbSize";
            this.tbSize.Size = new System.Drawing.Size(228, 45);
            this.tbSize.SmallChange = 30;
            this.tbSize.TabIndex = 10;
            this.tbSize.Scroll += new System.EventHandler(this.tbSize_Scroll);
            // 
            // gbxRadio
            // 
            this.gbxRadio.Controls.Add(this.pbxToolEraser);
            this.gbxRadio.Controls.Add(this.pbxToolLine);
            this.gbxRadio.Controls.Add(this.pbxToolSquare);
            this.gbxRadio.Controls.Add(this.pbxToolPen);
            this.gbxRadio.Location = new System.Drawing.Point(24, 23);
            this.gbxRadio.Name = "gbxRadio";
            this.gbxRadio.Size = new System.Drawing.Size(373, 89);
            this.gbxRadio.TabIndex = 13;
            this.gbxRadio.TabStop = false;
            this.gbxRadio.Text = "Verktyg";
            // 
            // pbxToolEraser
            // 
            this.pbxToolEraser.BackgroundImage = global::paintXS.Properties.Resources.eraser;
            this.pbxToolEraser.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolEraser.Location = new System.Drawing.Point(225, 19);
            this.pbxToolEraser.Name = "pbxToolEraser";
            this.pbxToolEraser.Size = new System.Drawing.Size(52, 50);
            this.pbxToolEraser.TabIndex = 3;
            this.pbxToolEraser.TabStop = false;
            this.pbxToolEraser.Click += new System.EventHandler(this.pbxToolEraser_Click);
            // 
            // pbxToolLine
            // 
            this.pbxToolLine.BackgroundImage = global::paintXS.Properties.Resources.line;
            this.pbxToolLine.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolLine.Location = new System.Drawing.Point(152, 21);
            this.pbxToolLine.Name = "pbxToolLine";
            this.pbxToolLine.Size = new System.Drawing.Size(52, 50);
            this.pbxToolLine.TabIndex = 2;
            this.pbxToolLine.TabStop = false;
            this.pbxToolLine.Click += new System.EventHandler(this.pbxToolLine_Click);
            // 
            // pbxToolSquare
            // 
            this.pbxToolSquare.BackgroundImage = global::paintXS.Properties.Resources.square;
            this.pbxToolSquare.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolSquare.Location = new System.Drawing.Point(77, 21);
            this.pbxToolSquare.Name = "pbxToolSquare";
            this.pbxToolSquare.Size = new System.Drawing.Size(52, 50);
            this.pbxToolSquare.TabIndex = 1;
            this.pbxToolSquare.TabStop = false;
            this.pbxToolSquare.Click += new System.EventHandler(this.pbxToolSquare_Click);
            // 
            // pbxToolPen
            // 
            this.pbxToolPen.BackgroundImage = global::paintXS.Properties.Resources.pen;
            this.pbxToolPen.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolPen.Location = new System.Drawing.Point(6, 21);
            this.pbxToolPen.Name = "pbxToolPen";
            this.pbxToolPen.Size = new System.Drawing.Size(52, 50);
            this.pbxToolPen.TabIndex = 0;
            this.pbxToolPen.TabStop = false;
            this.pbxToolPen.Click += new System.EventHandler(this.pbxToolPen_Click);
            // 
            // pbxTrash
            // 
            this.pbxTrash.BackgroundImage = global::paintXS.Properties.Resources.trash;
            this.pbxTrash.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxTrash.Location = new System.Drawing.Point(1106, 12);
            this.pbxTrash.Name = "pbxTrash";
            this.pbxTrash.Size = new System.Drawing.Size(93, 89);
            this.pbxTrash.TabIndex = 14;
            this.pbxTrash.TabStop = false;
            this.pbxTrash.Click += new System.EventHandler(this.pbxTrash_Click);
            // 
            // pbColourSelection
            // 
            this.pbColourSelection.BackColor = System.Drawing.Color.Black;
            this.pbColourSelection.Location = new System.Drawing.Point(808, 34);
            this.pbColourSelection.Name = "pbColourSelection";
            this.pbColourSelection.Size = new System.Drawing.Size(185, 60);
            this.pbColourSelection.TabIndex = 3;
            this.pbColourSelection.TabStop = false;
            this.pbColourSelection.Click += new System.EventHandler(this.pbColourSelection_Click);
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
            // pictureBox2
            // 
            this.pictureBox2.Location = new System.Drawing.Point(976, 23);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(100, 71);
            this.pictureBox2.TabIndex = 4;
            this.pictureBox2.TabStop = false;
            // 
            // FRMPaintProgram
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1221, 671);
            this.Controls.Add(this.pbxTrash);
            this.Controls.Add(this.gbxRadio);
            this.Controls.Add(this.pbColourSelection);
            this.Controls.Add(this.tbSize);
            this.Controls.Add(this.pbxPaintArea);
            this.Name = "FRMPaintProgram";
            this.Text = "paintXS";
            ((System.ComponentModel.ISupportInitialize)(this.tbSize)).EndInit();
            this.gbxRadio.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolEraser)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolLine)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolSquare)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolPen)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxTrash)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbColourSelection)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxPaintArea)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pbxPaintArea;
        private System.Windows.Forms.TrackBar tbSize;
        private System.Windows.Forms.ColorDialog colorDialog;
        private System.Windows.Forms.PictureBox pbColourSelection;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.GroupBox gbxRadio;
        private System.Windows.Forms.PictureBox pbxToolPen;
        private System.Windows.Forms.PictureBox pbxToolSquare;
        private System.Windows.Forms.PictureBox pbxToolLine;
        private System.Windows.Forms.PictureBox pbxToolEraser;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pbxTrash;
    }
}

