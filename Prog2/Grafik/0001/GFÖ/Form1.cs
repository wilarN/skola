using System;
using System.Windows.Forms;
using System.Drawing;

namespace GFÖ
{
    public partial class Form1 : Form
    {
        private Circle small01; // red
        private Circle small02Divider; // black
        private Circle small03Divider; // black
        private Circle medium01; // greenyellow
        private Circle smallSmall01; // smallest circle center
        private Circle smallSmall01Divider; // behind the smallest center dot
        private Circle smallSmall01Yellow;
        private Circle smallSmall01YellowDivider;
        private Circle medium02;

        public Form1()
        {
            InitializeComponent();

            small01 = new Circle(300, 300, 50);
            small02Divider = new Circle(300, 300, 53);
            medium01 = new Circle(300, 300, 100);
            small03Divider = new Circle(300, 300, 103);
            smallSmall01 = new Circle(300, 300, 10);
            smallSmall01Divider = new Circle(300, 300, 13);
            smallSmall01Yellow = new Circle(300, 300, 20);
            smallSmall01YellowDivider = new Circle(300, 300, 23);
            // Medium 02 continue
        }

        protected override void OnPaint(PaintEventArgs e)
        {

            Brush fillBrushGY = new SolidBrush(Color.GreenYellow);
            Brush fillBrushRed = new SolidBrush(Color.Red);
            Brush fillBrushBlack = new SolidBrush(Color.Black);
            Brush FillBrushYellow = new SolidBrush(Color.Yellow);


            medium01.renderWithOutline(fillBrushGY, fillBrushBlack, e, small03Divider);

            small01.renderWithOutline(fillBrushRed, fillBrushBlack, e, small02Divider);

            smallSmall01Yellow.renderWithOutline(FillBrushYellow, fillBrushBlack, e, smallSmall01YellowDivider);

            smallSmall01.renderWithOutline(fillBrushRed, fillBrushBlack, e, smallSmall01Divider);


            // Cleanup
            fillBrushGY.Dispose();
            fillBrushRed.Dispose();
            fillBrushBlack.Dispose();
            FillBrushYellow.Dispose();
        }

    }
}

