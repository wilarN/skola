using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _7._2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            int ageUser = int.Parse(tbxMainInput.Text);
            int price = 10;
            if(ageUser >= 15 && ageUser <= 65)
            {
                price = 20;
            }
            lblResultat.Text = "Your Price: " + price.ToString() + " €";
        }
    }
}
