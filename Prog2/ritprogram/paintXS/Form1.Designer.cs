
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FRMPaintProgram));
            this.tbSize = new System.Windows.Forms.TrackBar();
            this.colorDialog = new System.Windows.Forms.ColorDialog();
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.pbxTrash = new System.Windows.Forms.PictureBox();
            this.pbColourSelection = new System.Windows.Forms.PictureBox();
            this.pbxPaintArea = new System.Windows.Forms.PictureBox();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.pbxToolPen = new System.Windows.Forms.PictureBox();
            this.pbxToolSquare = new System.Windows.Forms.PictureBox();
            this.pbxToolLine = new System.Windows.Forms.PictureBox();
            this.pbxToolEraser = new System.Windows.Forms.PictureBox();
            this.gbxRadio = new System.Windows.Forms.GroupBox();
            this.pbxToolFilledRect = new System.Windows.Forms.PictureBox();
            this.pbxToolCircle = new System.Windows.Forms.PictureBox();
            this.pbxExportArea = new System.Windows.Forms.PictureBox();
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.pbxImport = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.tbSize)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxTrash)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbColourSelection)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxPaintArea)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolPen)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolSquare)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolLine)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolEraser)).BeginInit();
            this.gbxRadio.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolFilledRect)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolCircle)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxExportArea)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxImport)).BeginInit();
            this.SuspendLayout();
            // 
            // tbSize
            // 
            this.tbSize.Cursor = System.Windows.Forms.Cursors.Hand;
            this.tbSize.Location = new System.Drawing.Point(488, 44);
            this.tbSize.Maximum = 100;
            this.tbSize.Name = "tbSize";
            this.tbSize.Size = new System.Drawing.Size(170, 45);
            this.tbSize.SmallChange = 30;
            this.tbSize.TabIndex = 10;
            this.tbSize.Scroll += new System.EventHandler(this.tbSize_Scroll);
            // 
            // pbxTrash
            // 
            this.pbxTrash.BackColor = System.Drawing.Color.Transparent;
            this.pbxTrash.BackgroundImage = global::paintXS.Properties.Resources.trash;
            this.pbxTrash.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxTrash.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxTrash.Location = new System.Drawing.Point(1085, 23);
            this.pbxTrash.Name = "pbxTrash";
            this.pbxTrash.Size = new System.Drawing.Size(95, 89);
            this.pbxTrash.TabIndex = 14;
            this.pbxTrash.TabStop = false;
            this.pbxTrash.Click += new System.EventHandler(this.pbxTrash_Click);
            this.pbxTrash.MouseEnter += new System.EventHandler(this.pbxTrash_MouseEnter);
            this.pbxTrash.MouseLeave += new System.EventHandler(this.pbxTrash_MouseLeave);
            // 
            // pbColourSelection
            // 
            this.pbColourSelection.BackColor = System.Drawing.Color.Black;
            this.pbColourSelection.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pbColourSelection.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbColourSelection.Location = new System.Drawing.Point(703, 42);
            this.pbColourSelection.Name = "pbColourSelection";
            this.pbColourSelection.Size = new System.Drawing.Size(114, 50);
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
            // pbxToolPen
            // 
            this.pbxToolPen.BackgroundImage = global::paintXS.Properties.Resources.pen;
            this.pbxToolPen.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolPen.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxToolPen.Location = new System.Drawing.Point(6, 21);
            this.pbxToolPen.Name = "pbxToolPen";
            this.pbxToolPen.Size = new System.Drawing.Size(52, 50);
            this.pbxToolPen.TabIndex = 0;
            this.pbxToolPen.TabStop = false;
            this.pbxToolPen.Click += new System.EventHandler(this.pbxToolPen_Click);
            // 
            // pbxToolSquare
            // 
            this.pbxToolSquare.BackgroundImage = global::paintXS.Properties.Resources.square;
            this.pbxToolSquare.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolSquare.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxToolSquare.Location = new System.Drawing.Point(77, 21);
            this.pbxToolSquare.Name = "pbxToolSquare";
            this.pbxToolSquare.Size = new System.Drawing.Size(52, 50);
            this.pbxToolSquare.TabIndex = 1;
            this.pbxToolSquare.TabStop = false;
            this.pbxToolSquare.Click += new System.EventHandler(this.pbxToolSquare_Click);
            // 
            // pbxToolLine
            // 
            this.pbxToolLine.BackgroundImage = global::paintXS.Properties.Resources.line;
            this.pbxToolLine.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolLine.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxToolLine.Location = new System.Drawing.Point(152, 21);
            this.pbxToolLine.Name = "pbxToolLine";
            this.pbxToolLine.Size = new System.Drawing.Size(52, 50);
            this.pbxToolLine.TabIndex = 2;
            this.pbxToolLine.TabStop = false;
            this.pbxToolLine.Click += new System.EventHandler(this.pbxToolLine_Click);
            // 
            // pbxToolEraser
            // 
            this.pbxToolEraser.BackgroundImage = global::paintXS.Properties.Resources.eraser;
            this.pbxToolEraser.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolEraser.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxToolEraser.Location = new System.Drawing.Point(363, 19);
            this.pbxToolEraser.Name = "pbxToolEraser";
            this.pbxToolEraser.Size = new System.Drawing.Size(52, 50);
            this.pbxToolEraser.TabIndex = 3;
            this.pbxToolEraser.TabStop = false;
            this.pbxToolEraser.Click += new System.EventHandler(this.pbxToolEraser_Click);
            // 
            // gbxRadio
            // 
            this.gbxRadio.BackColor = System.Drawing.Color.Transparent;
            this.gbxRadio.BackgroundImage = global::paintXS.Properties.Resources.wood_rep02;
            this.gbxRadio.Controls.Add(this.pbxToolFilledRect);
            this.gbxRadio.Controls.Add(this.pbxToolCircle);
            this.gbxRadio.Controls.Add(this.pbxToolEraser);
            this.gbxRadio.Controls.Add(this.pbxToolLine);
            this.gbxRadio.Controls.Add(this.pbxToolSquare);
            this.gbxRadio.Controls.Add(this.pbxToolPen);
            this.gbxRadio.ForeColor = System.Drawing.SystemColors.ButtonFace;
            this.gbxRadio.Location = new System.Drawing.Point(24, 23);
            this.gbxRadio.Name = "gbxRadio";
            this.gbxRadio.Size = new System.Drawing.Size(424, 89);
            this.gbxRadio.TabIndex = 13;
            this.gbxRadio.TabStop = false;
            this.gbxRadio.Text = "Verktyg";
            // 
            // pbxToolFilledRect
            // 
            this.pbxToolFilledRect.BackgroundImage = global::paintXS.Properties.Resources.rectangle_filled;
            this.pbxToolFilledRect.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolFilledRect.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxToolFilledRect.Location = new System.Drawing.Point(291, 19);
            this.pbxToolFilledRect.Name = "pbxToolFilledRect";
            this.pbxToolFilledRect.Size = new System.Drawing.Size(52, 50);
            this.pbxToolFilledRect.TabIndex = 5;
            this.pbxToolFilledRect.TabStop = false;
            this.pbxToolFilledRect.Click += new System.EventHandler(this.pbxToolFilledRect_Click);
            // 
            // pbxToolCircle
            // 
            this.pbxToolCircle.BackgroundImage = global::paintXS.Properties.Resources.circle;
            this.pbxToolCircle.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxToolCircle.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxToolCircle.Location = new System.Drawing.Point(224, 19);
            this.pbxToolCircle.Name = "pbxToolCircle";
            this.pbxToolCircle.Size = new System.Drawing.Size(52, 50);
            this.pbxToolCircle.TabIndex = 4;
            this.pbxToolCircle.TabStop = false;
            this.pbxToolCircle.Click += new System.EventHandler(this.pbxToolCircle_Click);
            // 
            // pbxExportArea
            // 
            this.pbxExportArea.BackColor = System.Drawing.Color.Transparent;
            this.pbxExportArea.BackgroundImage = global::paintXS.Properties.Resources.save;
            this.pbxExportArea.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxExportArea.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxExportArea.Location = new System.Drawing.Point(978, 23);
            this.pbxExportArea.Name = "pbxExportArea";
            this.pbxExportArea.Size = new System.Drawing.Size(87, 89);
            this.pbxExportArea.TabIndex = 15;
            this.pbxExportArea.TabStop = false;
            this.pbxExportArea.Click += new System.EventHandler(this.pbxExportArea_Click);
            this.pbxExportArea.MouseEnter += new System.EventHandler(this.pbxExportArea_MouseEnter);
            this.pbxExportArea.MouseLeave += new System.EventHandler(this.pbxExportArea_MouseLeave);
            // 
            // pbxImport
            // 
            this.pbxImport.BackColor = System.Drawing.Color.Transparent;
            this.pbxImport.BackgroundImage = global::paintXS.Properties.Resources.import;
            this.pbxImport.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pbxImport.Cursor = System.Windows.Forms.Cursors.Hand;
            this.pbxImport.Location = new System.Drawing.Point(849, 23);
            this.pbxImport.Name = "pbxImport";
            this.pbxImport.Size = new System.Drawing.Size(87, 89);
            this.pbxImport.TabIndex = 16;
            this.pbxImport.TabStop = false;
            this.pbxImport.Click += new System.EventHandler(this.pbxImport_Click);
            this.pbxImport.MouseEnter += new System.EventHandler(this.pbxImport_MouseEnter);
            this.pbxImport.MouseLeave += new System.EventHandler(this.pbxImport_MouseLeave);
            // 
            // FRMPaintProgram
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.BackgroundImage = global::paintXS.Properties.Resources.wood_rep01;
            this.ClientSize = new System.Drawing.Size(1221, 671);
            this.Controls.Add(this.pbxImport);
            this.Controls.Add(this.pbxExportArea);
            this.Controls.Add(this.pbxTrash);
            this.Controls.Add(this.gbxRadio);
            this.Controls.Add(this.pbColourSelection);
            this.Controls.Add(this.tbSize);
            this.Controls.Add(this.pbxPaintArea);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "FRMPaintProgram";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "paintXS";
            ((System.ComponentModel.ISupportInitialize)(this.tbSize)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxTrash)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbColourSelection)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxPaintArea)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolPen)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolSquare)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolLine)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolEraser)).EndInit();
            this.gbxRadio.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolFilledRect)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxToolCircle)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxExportArea)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbxImport)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pbxPaintArea;
        private System.Windows.Forms.TrackBar tbSize;
        private System.Windows.Forms.ColorDialog colorDialog;
        private System.Windows.Forms.PictureBox pbColourSelection;
        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.PictureBox pbxTrash;
        private System.Windows.Forms.PictureBox pbxToolPen;
        private System.Windows.Forms.PictureBox pbxToolSquare;
        private System.Windows.Forms.PictureBox pbxToolLine;
        private System.Windows.Forms.PictureBox pbxToolEraser;
        private System.Windows.Forms.GroupBox gbxRadio;
        private System.Windows.Forms.PictureBox pbxExportArea;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.PictureBox pbxToolCircle;
        private System.Windows.Forms.PictureBox pbxToolFilledRect;
        private System.Windows.Forms.PictureBox pbxImport;
    }
}

