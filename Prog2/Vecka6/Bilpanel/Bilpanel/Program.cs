using System;
using Bilpanel;

namespace Bilpanel
{

    class Program
    {
        static void Main(string[] args)
        {
            Car volvo01 = new Car(model_constr:"Volvo", maxFuelL_constr:60);
            volvo01.drive(10);
            Console.WriteLine(volvo01.howMuchCanIFuelUpFor());
            volvo01.fuel(5);
            Console.WriteLine("-+-+-+-+-+-+-+-+-+");
            volvo01.summary();
            Console.ReadKey();
        }
    }
}
