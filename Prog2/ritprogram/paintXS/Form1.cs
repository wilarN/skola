using System;
using System.Drawing;
using System.Windows.Forms;

namespace paintXS
{
    public partial class FRMPaintProgram : Form
    {
        // Om användaren aktivt ritar
        private bool isCurrentlyDrawing = false;

        // Håller koll på tidigare point som ritats på
        private Point previousPoint;

        // En bitmap för att spara ritdata
        private Bitmap drawingSurface = new Bitmap(1197, 530);

        // Storlek på brush --> Default size 3
        private int paintSize = 3;

        // Färg --> Default Svart
        private Color mainColor = Color.Black;

        // Current tool
        /*
         CASES:
        1. Normal pen
        2. Square
        3. Eraser
         */
        private int currentTool = 3;

        // Add variables to store the starting point and ending point of the rectangle
        private Point startPoint;
        private Point endPoint;

        public FRMPaintProgram()
        {
            InitializeComponent();

            // 
            InitializeDrawingSurface();
        }

        // Metod för att skapa ett ritområde genom att rensa det till vit färg.
        private void InitializeDrawingSurface()
        {
            using (Graphics g = Graphics.FromImage(drawingSurface))
            {
                g.Clear(Color.White);
            }
        }

        private void pbxPaintArea_MouseDown(object sender, MouseEventArgs e)
        {
            switch (currentTool)
            {
                case 1: case 3:
                    isCurrentlyDrawing = true;
                    previousPoint = e.Location;         // Sparar positionen där muspekaren befann sig när ritningen påbörjades i previousPoint 
                    lblDebugText.Text = "KLICKAR";
                    break;
                case 2:
                    previousPoint = e.Location;
                    startPoint = e.Location;
                    isCurrentlyDrawing = true;
                    break;
                default:
                    break;
            }
        }

        private void pbxPaintArea_MouseUp(object sender, MouseEventArgs e)
        {
            switch (currentTool)
            {
                case 1: case 3:
                    isCurrentlyDrawing = false;
                    lblDebugText.Text = "LYFTER";
                    break;
                case 2:
                    using (Graphics g = Graphics.FromImage(drawingSurface))
                    {
                        // Square box
                        Pen pen = new Pen(mainColor, paintSize);

                        int width = Math.Abs(endPoint.X - startPoint.X);
                        int height = Math.Abs(endPoint.Y - startPoint.Y);
                        int x = Math.Min(startPoint.X, endPoint.X);
                        int y = Math.Min(startPoint.Y, endPoint.Y);
                        Rectangle rect = new Rectangle(x, y, width, height);

                        g.DrawRectangle(pen, rect);

                        pen.Dispose();
                        isCurrentlyDrawing = false;

                        startPoint = e.Location;
                        endPoint = e.Location;
                        pbxPaintArea.Invalidate();
                        break;
                    }
                default:
                    break;
            }
        }

        private void pbxPaintArea_Paint(object sender, PaintEventArgs e)
        {
            // Rita inom paintArea
            e.Graphics.DrawImage(drawingSurface, Point.Empty);

            // Draw rectangle if using the rectangle tool
            if (currentTool == 2 && startPoint != null && endPoint != null)
            {
                Pen pen = new Pen(mainColor, paintSize);


                int width = Math.Abs(endPoint.X - startPoint.X);
                int height = Math.Abs(endPoint.Y - startPoint.Y);

                int x = Math.Min(startPoint.X, endPoint.X);
                int y = Math.Min(startPoint.Y, endPoint.Y);
                
                Rectangle rect = new Rectangle(x, y, width, height);
                e.Graphics.DrawRectangle(pen, rect);
            }
        }

        private void pbxPaintArea_MouseMove(object sender, MouseEventArgs e)
        {
            if (isCurrentlyDrawing)
            {
                using (Graphics g = Graphics.FromImage(drawingSurface))
                {
                    if(currentTool == 3) {
                        mainColor = Color.White;
                    }
                    switch (currentTool)
                    {
                        case 1: case 3:
                            // Normal pen
                            // Skapa en penna
                            Pen pen = new Pen(mainColor, paintSize);
                            pen.StartCap = System.Drawing.Drawing2D.LineCap.Round;
                            pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;

                            // Rita en linje från föregående musposition till nuvarande musposition
                            g.DrawLine(pen, previousPoint, e.Location);
                            pen.Dispose();

                            previousPoint = e.Location;

                            // Uppdatera PictureBox för att visa de ändringar som gjorts på ritområdet
                            pbxPaintArea.Invalidate();
                            break;
                        case 2:
                            endPoint = e.Location;
                            pbxPaintArea.Invalidate(); // Force the paint area to redraw
                            break;
                        default:
                            break;
                    }

                }

            }
        }

        private void tbSize_Scroll(object sender, EventArgs e)
        {
            paintSize = tbSize.Value;
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
                mainColor = colorDialog.Color;
            }
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            using (Graphics g = Graphics.FromImage(drawingSurface))
            {
                g.Clear(Color.White);
                pbxPaintArea.Invalidate();
            }
        }
    }
}
