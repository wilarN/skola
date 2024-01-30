using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace V3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            #region Uppgift_1
            Console.WriteLine("- Uppgift 1 -");
            double value1 = 3.14;
            double value2 = 2.5;

            double combined = value1 * value2;
            Console.WriteLine($"Resultat 1: {combined}");

            double numMax = Math.Max(5, 10);
            Console.WriteLine($"Högsta talet av 5 och 10 är: {numMax}");

            double numMax2 = Math.Max(value1, value2);
            Console.WriteLine($"Högst värdet av {value1} & {value2} är: {numMax2}");
            #endregion

            // -----------------------
            Console.WriteLine("-------------");
            // -----------------------

            #region Uppgift_2
            Console.WriteLine("- Uppgift 2 -");
            string unit = "m";
            double radie = 4.0;
            double area = Math.PI * Math.Pow(radie, 2);

            Console.WriteLine($"Radien är {radie} och området är {area} {unit}^2.");

            // TID ÖVER
            Console.WriteLine($"Värdet {radie} på radien ger en area på {area} {unit}^2.");
            Console.ReadKey();
            #endregion
        }
    }
}
