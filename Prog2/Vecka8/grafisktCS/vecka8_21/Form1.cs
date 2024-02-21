using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vecka8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnClickHere_Click(object sender, EventArgs e)
        {
            // Här visas messageboxen upp när "Klicka här" knappen har klickats på.
            MessageBox.Show(
                "Mitt första program",
                "Meddelande",
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Information
                );
        }
    }
}
