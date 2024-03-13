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
        private Circle medium02Divider;
        private double widthModifier;

        private Brush fillBrushGY;
        private Brush fillBrushRed;
        private Brush fillBrushBlack;
        private Brush fillBrushYellow;
        private Brush fillBrushOrange;

        public Form1()
        {
            InitializeComponent();

            float xPlacement = this.Size.Width / 2;
            float yPlacement = this.Size.Height / 2;
            double widthModifier = 1;

            small01 = new Circle(xPlacement, yPlacement, 50 * (float)widthModifier);
            small02Divider = new Circle(xPlacement, yPlacement, 53 * (float)widthModifier);
            medium01 = new Circle(xPlacement, yPlacement, 100 * (float)widthModifier);
            small03Divider = new Circle(xPlacement, yPlacement, 103 * (float)widthModifier);
            smallSmall01 = new Circle(xPlacement, yPlacement, 10 * (float)widthModifier);
            smallSmall01Divider = new Circle(xPlacement, yPlacement, 13 * (float)widthModifier);
            smallSmall01Yellow = new Circle(xPlacement, yPlacement, 20 * (float)widthModifier);
            smallSmall01YellowDivider = new Circle(xPlacement, yPlacement, 23 * (float)widthModifier);
            medium02 = new Circle(xPlacement, yPlacement, 75 * (float)widthModifier);
            medium02Divider = new Circle(xPlacement, yPlacement, 78 * (float)widthModifier);

            fillBrushGY = new SolidBrush(Color.GreenYellow);
            fillBrushRed = new SolidBrush(Color.Red);
            fillBrushBlack = new SolidBrush(Color.Black);
            fillBrushYellow = new SolidBrush(Color.Yellow);
            fillBrushOrange = new SolidBrush(Color.Orange);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            fillBrushGY = new SolidBrush(Color.GreenYellow);
            fillBrushRed = new SolidBrush(Color.Red);
            fillBrushBlack = new SolidBrush(Color.Black);
            fillBrushYellow = new SolidBrush(Color.Yellow);
            fillBrushOrange = new SolidBrush(Color.Orange);

            small01.radius = small01.radius * (float)widthModifier;

            medium01.renderWithOutline(fillBrushGY, fillBrushBlack, e, small03Divider);
            medium02.renderWithOutline(fillBrushOrange, fillBrushBlack, e, medium02Divider);

            small01.renderWithOutline(fillBrushRed, fillBrushBlack, e, small02Divider);


            smallSmall01Yellow.renderWithOutline(fillBrushYellow, fillBrushBlack, e, smallSmall01YellowDivider);

            smallSmall01.renderWithOutline(fillBrushRed, fillBrushBlack, e, smallSmall01Divider);

            fillBrushGY.Dispose();
            fillBrushRed.Dispose();
            fillBrushBlack.Dispose();
            fillBrushYellow.Dispose();
            fillBrushOrange.Dispose();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(double.TryParse(tbxRadius.Text, out double newValue))
            {
                widthModifier = Math.Abs(newValue);
                Invalidate();
            }
        }
    }
}

