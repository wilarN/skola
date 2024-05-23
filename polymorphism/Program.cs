using System;

namespace poly
{
    class Program
    {
        static void Main(string[] args)
        {
            myClasses.animal mainAnimal = new myClasses.animal();
            mainAnimal.sound();

            myClasses.pig mainPig = new myClasses.pig();
            mainPig.sound();

            Console.ReadKey();
        }
    }
}
