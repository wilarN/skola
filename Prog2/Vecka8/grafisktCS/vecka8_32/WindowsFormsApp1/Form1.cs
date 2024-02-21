using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(tbxTal1.Text != "" || tbxTal2.Text != "")
            {
                double tal1 = double.Parse(tbxTal1.Text);
                double tal2 = double.Parse(tbxTal2.Text);
                double sum = tal1 + tal2;
                string text = sum.ToString();
                lblSum.Text = "Summan av talen är: " + text;
            }
        }
    }
}
