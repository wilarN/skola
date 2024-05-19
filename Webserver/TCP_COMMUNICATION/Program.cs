using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace tcpCommunication
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            // Client 1 for testing.
            Task.Run(() =>
            {
                Application.Run(new login());
            });

            // Client 2 for testing.
            Task.Run(() =>
            {
                Application.Run(new login());
            });

            // Client n, add more as you see fit.
            //Task.Run(() =>
            //{
            //    Application.Run(new login());
            //});


            // Actual chatserver.
            Application.Run(new server());

        }
    }
}
