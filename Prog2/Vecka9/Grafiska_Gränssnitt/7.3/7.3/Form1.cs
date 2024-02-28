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
        Random rand = new Random();

        public Form1()
        {
            InitializeComponent();
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            string num = rand.Next(1, 7).ToString();
            lblResultat.Text = num;
            if(num == "6")
            {
                MessageBox.Show(btnOK, "Grattis! Du fick en sexa!");
            }
        }
    }
}
