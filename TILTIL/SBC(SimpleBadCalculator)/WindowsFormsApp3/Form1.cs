using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_MouseClick(object sender, MouseEventArgs e)
        {
            if (textBox3.Text == "ADDITION")
            {
                MessageBox.Show(Convert.ToString(Convert.ToDouble(textBox1.Text) + Convert.ToDouble(textBox2.Text)));
            }
            else if(textBox3.Text == "MULTIPLICATION")
            {
                MessageBox.Show(Convert.ToString(Convert.ToDouble(textBox1.Text) * Convert.ToDouble(textBox2.Text)));

            }
            else if(textBox3.Text == "SUBTRACTION")
            {
                MessageBox.Show(Convert.ToString(Convert.ToDouble(textBox1.Text) - Convert.ToDouble(textBox2.Text)));

            }else if(textBox3.Text == "DIVITION")
            {
                MessageBox.Show(Convert.ToString(Convert.ToDouble(textBox1.Text) / Convert.ToDouble(textBox2.Text)));
            }
            else
            {
                MessageBox.Show("Please select a valid calculation type and make sure the numbers you're trying to use are valid.");
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
