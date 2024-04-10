using System;
using System.Drawing;
using System.Windows.Forms;

namespace paintXS
{
    public partial class FRMPaintProgram : Form
    {
        // Create mainPen object
        paintXSPen mainPen = new paintXSPen();

        public FRMPaintProgram()
        {
            InitializeComponent();
            InitializeDrawingSurface();
        }

        // If backup color is needed, for example when using eraser, the backup color will be fetched.
        private bool backupColorFetcher()
        {
            // Checks if the backup color is in use.
            if (mainPen.useBackupColor)
            {
                mainPen.mainColor = mainPen.backupColor;
                mainPen.useBackupColor = false;
                return true;
            }
            else
            {
                return false;
            }
        }

        // Method for creating a drawing surface by clearing out with white.
        private void InitializeDrawingSurface()
        {
            using (Graphics g = Graphics.FromImage(mainPen.drawingSurface))
            {
                g.Clear(Color.White);
            }
        }

        // When MouseDown on paintarea:
        private void pbxPaintArea_MouseDown(object sender, MouseEventArgs e)
        {
            switch (mainPen.currentTool)
            {
                case 1: case 4:
                    mainPen.isCurrentlyDrawing = true;
                    mainPen.previousPoint = e.Location; // Sparar positionen där muspekaren befann sig när ritningen påbörjades i previousPoint 
                    break;
                case 2: case 3:
                    mainPen.previousPoint = e.Location;
                    mainPen.startPoint = e.Location;
                    mainPen.isCurrentlyDrawing = true;
                    break;
                default:
                    break;
            }
        }

        // When MouseUp on paintarea:
        private void pbxPaintArea_MouseUp(object sender, MouseEventArgs e)
        {
            switch (mainPen.currentTool)
            {
                case 1: case 4:
                    mainPen.isCurrentlyDrawing = false;
                    break;
                case 2:
                    using (Graphics g = Graphics.FromImage(mainPen.drawingSurface))
                    {
                        // Square box
                        Pen pen = new Pen(mainPen.mainColor, mainPen.paintSize);

                        int width = Math.Abs(mainPen.endPoint.X - mainPen.startPoint.X);
                        int height = Math.Abs(mainPen.endPoint.Y - mainPen.startPoint.Y);
                        int x = Math.Min(mainPen.startPoint.X, mainPen.endPoint.X);
                        int y = Math.Min(mainPen.startPoint.Y, mainPen.endPoint.Y);
                        Rectangle rect = new Rectangle(x, y, width, height);

                        g.DrawRectangle(pen, rect);

                        pen.Dispose();
                        mainPen.isCurrentlyDrawing = false;

                        mainPen.startPoint = e.Location;
                        mainPen.endPoint = e.Location;
                        pbxPaintArea.Invalidate();
                        break;
                    }
                case 3:
                    using (Graphics g = Graphics.FromImage(mainPen.drawingSurface))
                    {
                        // Square box
                        Pen pen = new Pen(mainPen.mainColor, mainPen.paintSize);
                        pen.StartCap = System.Drawing.Drawing2D.LineCap.Round;
                        pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;

                        g.DrawLine(pen, mainPen.startPoint, e.Location);

                        pen.Dispose();
                        mainPen.isCurrentlyDrawing = false;

                        mainPen.startPoint = e.Location;
                        mainPen.endPoint = e.Location;
                        pbxPaintArea.Invalidate();
                        break;
                    }
                default:
                    break;
            }
        }

        private void pbxPaintArea_Paint(object sender, PaintEventArgs e)
        {
            // Paint within the paintArea:
            e.Graphics.DrawImage(mainPen.drawingSurface, Point.Empty);

            // Draw rectangle if using the rectangle tool
            if (mainPen.currentTool == 2 && mainPen.startPoint != null && mainPen.endPoint != null)
            {
                Pen pen = new Pen(mainPen.mainColor, mainPen.paintSize);

                int width = Math.Abs(mainPen.endPoint.X - mainPen.startPoint.X);
                int height = Math.Abs(mainPen.endPoint.Y - mainPen.startPoint.Y);

                int x = Math.Min(mainPen.startPoint.X, mainPen.endPoint.X);
                int y = Math.Min(mainPen.startPoint.Y, mainPen.endPoint.Y);
                
                Rectangle rect = new Rectangle(x, y, width, height);
                e.Graphics.DrawRectangle(pen, rect);
            }
        }

        private void pbxPaintArea_MouseMove(object sender, MouseEventArgs e)
        {
            if (mainPen.isCurrentlyDrawing)
            {
                using (Graphics g = Graphics.FromImage(mainPen.drawingSurface))
                {
                    if(mainPen.currentTool == 4) {
                        mainPen.mainColor = Color.White;
                    }
                    switch (mainPen.currentTool)
                    {
                        case 1: case 4:
                            // Normal pen
                            // Create a pen
                            Pen pen = new Pen(mainPen.mainColor, mainPen.paintSize);
                            pen.StartCap = System.Drawing.Drawing2D.LineCap.Round;
                            pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;

                            g.DrawLine(pen, mainPen.previousPoint, e.Location);
                            pen.Dispose();

                            mainPen.previousPoint = e.Location;

                            // Update the PictureBox to show the changes that have been made within the paint area.
                            pbxPaintArea.Invalidate();
                            break;
                        case 2:
                            mainPen.endPoint = e.Location;
                            pbxPaintArea.Invalidate(); // Force the paint area to redraw
                            break;
                        default:
                            break;
                    }
                }
            }
        }

        // Pensize change from the slider.
        private void tbSize_Scroll(object sender, EventArgs e)
        {
            mainPen.paintSize = tbSize.Value;
        }

        private void pbColourSelection_Click(object sender, EventArgs e)
        {
            colorDialog.ShowHelp = true;
            colorDialog.AllowFullOpen = false;
            colorDialog.Color = pbColourSelection.ForeColor;


            if (colorDialog.ShowDialog() == DialogResult.OK)
            {
                pbColourSelection.ForeColor = colorDialog.Color;
                pbColourSelection.BackColor = colorDialog.Color;
                mainPen.mainColor = colorDialog.Color;
            }
        }

        // Clear out and repaint with white over the paint area.
        // "Trashbin" || "Clear out painting area"
        private void btnClear_Click(object sender, EventArgs e)
        {
            using (Graphics g = Graphics.FromImage(mainPen.drawingSurface))
            {
                // Actually perform the clearing.
                g.Clear(Color.White);
                pbxPaintArea.Invalidate();
            }
        }

        private void pbxToolPen_Click(object sender, EventArgs e)
        {
            backupColorFetcher();
            mainPen.currentTool = 1;
        }

        private void pbxToolSquare_Click(object sender, EventArgs e)
        {
            backupColorFetcher();
            mainPen.currentTool = 2;
        }

        private void pbxToolLine_Click(object sender, EventArgs e)
        {
            backupColorFetcher();
            mainPen.currentTool = 3;
        }

        private void pbxTrash_Click(object sender, EventArgs e)
        {
            using (Graphics g = Graphics.FromImage(mainPen.drawingSurface))
            {
                g.Clear(Color.White);
                pbxPaintArea.Invalidate();
            }
        }

        // Eraser tool, selection.
        private void pbxToolEraser_Click(object sender, EventArgs e)
        {
            mainPen.useBackupColor = true;
            mainPen.backupColor = mainPen.mainColor;
            // Set currentTool to the eraser.
            mainPen.currentTool = 4;
        }

        private void pbxExportArea_Click(object sender, EventArgs e)
        {
            // Export paintarea as PNG.
            mainPen.saveImageToDisk();
        }

        private void pbxExportArea_MouseEnter(object sender, EventArgs e)
        {
            pbxExportArea.Width += 10;
            pbxExportArea.Height += 10;
        }

        private void pbxExportArea_MouseLeave(object sender, EventArgs e)
        {
            pbxExportArea.Width -= 10;
            pbxExportArea.Height -= 10;
        }
        private void pbxTrash_MouseEnter(object sender, EventArgs e)
        {
            pbxTrash.Width += 10;
            pbxTrash.Height += 10;
        }

        private void pbxTrash_MouseLeave(object sender, EventArgs e)
        {
            pbxTrash.Width -= 10;
            pbxTrash.Height -= 10;
        }
    }
}
