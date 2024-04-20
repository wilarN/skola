using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Windows.Forms;
using System.IO;

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
            saveFileDialog.Filter = "PNG files (*.png)|*.png|JPEG files (*.jpg;*.jpeg)|*.jpg;*.jpeg";
            if (saveFileDialog.ShowDialog() == DialogResult.OK)
            {
                string fileName = saveFileDialog.FileName;
                string extension = Path.GetExtension(fileName).ToLower();

                ImageFormat imageFormat;

                switch (extension)
                {
                    case ".png":
                        imageFormat = ImageFormat.Png;
                        break;
                    case ".jpg":
                    case ".jpeg":
                        imageFormat = ImageFormat.Jpeg;
                        break;
                    case ".svg":
                        // .NET doesnt support svg for export.
                        MessageBox.Show("SVG saving is not supported.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        return false;
                    default:
                        // Unsupported file format
                        MessageBox.Show("Unsupported file format.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        return false;
                }

                drawingSurface.Save(fileName, imageFormat);
            }

            return true;
        }

        public bool importImageFromDisk(PictureBox pbxArea)
        {
            try
            {
                OpenFileDialog fileDialog = new OpenFileDialog();
                // Accept png, jpg, jpeg & svg
                fileDialog.Filter = "Image files (*.png;*.jpg;*.jpeg;*.svg)|*.png;*.jpg;*.jpeg;*.svg";
                if (fileDialog.ShowDialog() == DialogResult.OK)
                {
                    // Load the selected image
                    Bitmap loadedImage = new Bitmap(fileDialog.FileName);

                    // Scale the image to the size of the drawing area (PictureBox)
                    Bitmap scaledImage = new Bitmap(pbxArea.Width, pbxArea.Height);
                    using (Graphics g = Graphics.FromImage(scaledImage))
                    {
                        g.DrawImage(loadedImage, 0, 0, pbxArea.Width, pbxArea.Height);
                    }

                    // Assign the scaled image to drawingSurface and display it on the PictureBox
                    drawingSurface = scaledImage;
                    pbxArea.Image = drawingSurface;
                }
            }
            catch
            {
                return false;
            }
            return true;
        }
    }
}
