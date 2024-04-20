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
                case 2: case 3: case 5: case 7:
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
                        // Line
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
                case 5:
                    using(Graphics g = Graphics.FromImage(mainPen.drawingSurface))
                    {
                        // Circle
                        Pen pen = new Pen(mainPen.mainColor, mainPen.paintSize);
                        int width = Math.Abs(mainPen.endPoint.X - mainPen.startPoint.X);
                        int height = Math.Abs(mainPen.endPoint.Y - mainPen.startPoint.Y);
                        int x = Math.Min(mainPen.startPoint.X, mainPen.endPoint.X);
                        int y = Math.Min(mainPen.startPoint.Y, mainPen.endPoint.Y);

                        g.DrawEllipse(pen, x, y, width, height);
                        mainPen.isCurrentlyDrawing = false;

                        pen.Dispose();
                        mainPen.startPoint = e.Location;
                        mainPen.endPoint = e.Location;
                        pbxPaintArea.Invalidate();
                        break;
                    }
                case 6:
                    using (Graphics g = Graphics.FromImage(mainPen.drawingSurface))
                    {
                        // Square box
                        Pen pen = new Pen(mainPen.mainColor, mainPen.paintSize);

                        // Calculate the position of the star based on mouse drag
                        int width = Math.Abs(mainPen.endPoint.X - mainPen.startPoint.X);
                        int height = Math.Abs(mainPen.endPoint.Y - mainPen.startPoint.Y);
                        int x = Math.Min(mainPen.startPoint.X, mainPen.endPoint.X);
                        int y = Math.Min(mainPen.startPoint.Y, mainPen.endPoint.Y);

                        // Create points that define the star.
                        Point[] starPoints =
                        {
                            new Point(x + width / 2, y),
                            new Point(x + width * 7 / 10, y + height * 3 / 10),
                            new Point(x + width, y + height * 3 / 10),
                            new Point(x + width * 3 / 5, y + height * 6 / 10),
                            new Point(x + width * 8 / 10, y + height),
                            new Point(x + width / 2, y + height * 7 / 10),
                            new Point(x + width * 2 / 10, y + height),
                            new Point(x + width * 2 / 5, y + height * 6 / 10),
                            new Point(x, y + height * 3 / 10),
                            new Point(x + width * 3 / 10, y + height * 3 / 10)
                        };

                        // Draw star to screen.
                        g.DrawPolygon(pen, starPoints);
                        pen.Dispose();
                        mainPen.isCurrentlyDrawing = false;

                        mainPen.startPoint = e.Location;
                        mainPen.endPoint = e.Location;
                        pbxPaintArea.Invalidate();
                        break;
                    }
                case 7:
                    using (Graphics g = Graphics.FromImage(mainPen.drawingSurface))
                    {
                        // Filled Rectangle
                        Brush brush = new SolidBrush(mainPen.mainColor);

                    int width = Math.Abs(mainPen.endPoint.X - mainPen.startPoint.X);
                    int height = Math.Abs(mainPen.endPoint.Y - mainPen.startPoint.Y);
                    int x = Math.Min(mainPen.startPoint.X, mainPen.endPoint.X);
                    int y = Math.Min(mainPen.startPoint.Y, mainPen.endPoint.Y);
                    Rectangle rect = new Rectangle(x, y, width, height);

                    g.FillRectangle(brush, rect);

                    brush.Dispose();
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

            // Draw circle if using the circle tool
            if (mainPen.currentTool == 5 && mainPen.startPoint != null && mainPen.endPoint != null)
            {
                Pen pen = new Pen(mainPen.mainColor, mainPen.paintSize);
                int width = Math.Abs(mainPen.endPoint.X - mainPen.startPoint.X);
                int height = Math.Abs(mainPen.endPoint.Y - mainPen.startPoint.Y);
                int x = Math.Min(mainPen.startPoint.X, mainPen.endPoint.X);
                int y = Math.Min(mainPen.startPoint.Y, mainPen.endPoint.Y);

                e.Graphics.DrawEllipse(pen, x, y, width, height);
            }
            // Draw filled rect if using the fille drect tool
            if (mainPen.currentTool == 7 && mainPen.startPoint != null && mainPen.endPoint != null)
            {
                Brush brush = new SolidBrush(mainPen.mainColor);

                int width = Math.Abs(mainPen.endPoint.X - mainPen.startPoint.X);
                int height = Math.Abs(mainPen.endPoint.Y - mainPen.startPoint.Y);

                int x = Math.Min(mainPen.startPoint.X, mainPen.endPoint.X);
                int y = Math.Min(mainPen.startPoint.Y, mainPen.endPoint.Y);

                Rectangle rect = new Rectangle(x, y, width, height);
                e.Graphics.FillRectangle(brush, rect);
            }
            if(mainPen.currentTool == 3 && mainPen.startPoint != null && mainPen.endPoint != null)
            {
                // Line
                Pen pen = new Pen(mainPen.mainColor, mainPen.paintSize);
                pen.StartCap = System.Drawing.Drawing2D.LineCap.Round;
                pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;

                e.Graphics.DrawLine(pen, mainPen.startPoint, mainPen.endPoint);
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
                        case 2:  case 3: case 5:
                        case 7:
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

        // Tool at index 4 is further below.

        private void pbxToolCircle_Click(object sender, EventArgs e)
        {
            backupColorFetcher();
            mainPen.currentTool = 5;
        }

        private void pbxToolStar_Click(object sender, EventArgs e)
        {
            backupColorFetcher();
            mainPen.currentTool = 6;
        }

        private void pbxToolFilledRect_Click(object sender, EventArgs e)
        {
            backupColorFetcher();
            mainPen.currentTool = 7;
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

        private void pbxImport_Click(object sender, EventArgs e)
        {
            if (mainPen.importImageFromDisk(pbxPaintArea))
            {
                MessageBox.Show(
                "Successfully Imported Image!",
                "Import Successfull",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information
                );
            }
            else
            {
                MessageBox.Show(
                    "Error Importing Image",
                    "Error On Import",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning
                    );
            }
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

        private void pbxImport_MouseEnter(object sender, EventArgs e)
        {
            pbxImport.Width += 10;
            pbxImport.Height += 10;
        }

        private void pbxImport_MouseLeave(object sender, EventArgs e)
        {
            pbxImport.Width -= 10;
            pbxImport.Height -= 10;
        }

    }
}
