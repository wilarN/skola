using System;
using System.Windows.Forms;
using System.Drawing;

namespace GFÖ
{
    public class Circle
    {
        public double x;
        public double y;
        public double radius; 
        public Circle(float x_param, float y_param, float radius_param)
        {
            x = x_param;
            y = y_param;
            radius = radius_param;
        }

        public void renderWithOutline(Brush selectedBrush, Brush selectedBrushOutline, PaintEventArgs e, Circle outline)
        {
            // Outline
            e.Graphics.FillEllipse(selectedBrushOutline,
                (float)(outline.x - outline.radius), (float)(outline.y - outline.radius),
                (float)(outline.radius * 2), (float)(outline.radius * 2));

            // Bigger
            e.Graphics.FillEllipse(selectedBrush,
                (float)(x - radius), (float)(y - radius),
                (float)(radius * 2), (float)(radius * 2));
        }

        public void updateSize(float newRadius)
        {
            this.radius = newRadius;
        }
    }
}
