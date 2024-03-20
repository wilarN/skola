using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
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
        3. Delete
         */
        private int currentTool = 2;

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


        // Paintarea mouse down
        private void pbxPaintArea_MouseDown(object sender, MouseEventArgs e)
        {
            switch (currentTool)
            {
                case 1:
                    isCurrentlyDrawing = true;                   // Användaren har börjat rita                
                    previousPoint = e.Location;         // Sparar positionen där muspekaren befann sig när ritningen påbörjades i previousPoint 
                    lblDebugText.Text = "KLICKAR";
                    break;
                case 2:
                    previousPoint = e.Location;
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
                case 1:
                    isCurrentlyDrawing = false;                   // Användaren har börjat rita                
                    lblDebugText.Text = "LYFTER";
                    break;
                case 2:
                    using (Graphics g = Graphics.FromImage(drawingSurface))
                    {
                        // Square box
                        SolidBrush solidBrush = new SolidBrush(mainColor);

                        // Calculate the width and height of the square
                        int width = e.X - previousPoint.X;
                        int height = e.Y - previousPoint.Y;
                        int size = Math.Min(width, height);

                        g.FillRectangle(solidBrush, previousPoint.X, previousPoint.Y, size, size);

                        solidBrush.Dispose();
                        isCurrentlyDrawing = false;
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
        }

        private void pbxPaintArea_MouseMove(object sender, MouseEventArgs e)
        {
            if (isCurrentlyDrawing)
            {
                using (Graphics g = Graphics.FromImage(drawingSurface))
                {
                    switch (currentTool)
                    {
                        case 1:
                            // Normal pen
                            // Skapa en penna
                            Pen pen = new Pen(mainColor, paintSize);
                            pen.StartCap = System.Drawing.Drawing2D.LineCap.Round;
                            pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;

                            // Rita en linje från föregående musposition till nuvarande musposition med den svarta pennan
                            g.DrawLine(pen, previousPoint, e.Location);
                            pen.Dispose();

                            previousPoint = e.Location;

                            // Uppdatera PictureBox för att visa de ändringar som gjorts på ritområdet
                            pbxPaintArea.Invalidate();
                            break;
                        case 2:
                            break;
                        case 3:
                            // Eraser
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


            if(colorDialog.ShowDialog() == DialogResult.OK)
            {
                pbColourSelection.ForeColor = colorDialog.Color;
                pbColourSelection.BackColor = colorDialog.Color;
                mainColor = colorDialog.Color;
            }
        }
    }
}
