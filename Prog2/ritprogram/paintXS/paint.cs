using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Windows.Forms;

namespace paintXS
{
    class paintXSPen
    {

        // Om användaren aktivt ritar
        public bool isCurrentlyDrawing = false;

        // Håller koll på tidigare point som ritats på
        public Point previousPoint { get; set; }

        // En bitmap för att spara ritdata
        public Bitmap drawingSurface = new Bitmap(1197, 530);

        // Storlek på brush --> Default size 3
        public int paintSize = 3;

        // Färg --> Default Svart
        public Color mainColor = Color.Black;

        public bool useBackupColor = false;
        public Color backupColor { get; set; }


        /*
         CASES:
        1. Normal pen
        2. Square
        3. Line
        4. Eraser
        5. Circle
        6. Star shape
        7. Filled Square/Rectangle
         */
        public int currentTool = 1;

        // Add variables to store the starting point and ending point of the rectangle
        public Point startPoint;
        public Point endPoint;


        public bool saveImageToDisk()
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "PNG files (*.png)|*.png";
            if(saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                drawingSurface.Save(saveFileDialog.FileName, ImageFormat.Png);
            }

            return true;
        }
    }
}
