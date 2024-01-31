using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Yatzy
{
    class Program
    {
        static void IntroYatzy()
        {
            Console.Write(
                "Yatzy");
        }

        static void Main(string[] args)
        {
            Dictionary<string, int> yatzyPoints = new Dictionary<string, int>
            {
                { "Ones", 0 },
                { "Twos", 0 },
                { "Threes", 0 },
                { "Fours", 0 },
                { "Fives", 0 },
                { "Sixes", 0 },
                { "ThreeOfAKind", 0 },
                { "FourOfAKind", 0 },
                { "FullHouse", 0 },
                { "SmallStraight", 0 },
                { "LargeStraight", 0 },
                { "Yatzy", 0 },
                { "Chance", 0 }
            };

            IntroYatzy();
            
            

            Console.WriteLine(yatzyPoints["Ones"]);


            Console.ReadKey();

        }
    }
}
