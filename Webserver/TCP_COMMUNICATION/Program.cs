using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace tcpCommunication
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            Task.Run(() =>
            {
                Application.Run(new client());
            });

            Task.Run(() =>
            {
                Application.Run(new client());
            });

            Application.Run(new server());
            // Application.Run(new login());
        }
    }
}
