using System;

namespace Selektioner
{
    class Select
    {
        static void Main(string[] args)
        {
            Console.Write("How old are you?: ");
            int age = Convert.ToInt32(Console.ReadLine());
            float price;

            if (age < 18)
                // Kid
                price = 25.0f;
            else if (age >= 65)
                // Senior
                price = 35.0f;
            else
                // Full price
                price = 45.24f;

            Console.WriteLine("Your price is: " + price + "€");
            Console.ReadKey();


            Console.Clear();

            // Password stuff

            string password = "womp";

            while (true)
            {
                Console.Write("Password: ");
                if(Console.ReadLine() == password)
                {
                    Console.WriteLine("Välkommen in!");
                    break;
                }
                else
                {
                    Console.WriteLine("Wrong password...");
                }

            }


        }
    }
}
