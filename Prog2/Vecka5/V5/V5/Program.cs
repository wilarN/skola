using System;

namespace V5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            #region Uppgift_1
            int räknare = 0;
            int mål = 10;

            while(räknare < mål)
            {
                Console.WriteLine("Vi har inte nått målet med räknare på: " + räknare);
                räknare++;
            }
            Console.WriteLine("Målet är nått med " + räknare + "!");

            #endregion

            Console.WriteLine("-+-+-+-+-+-+-+-+-+-+-\n");

            #region Uppgift_2

            // Array of emails
            string[] emails = { "123@nfi.se", "2eqrf@nfi.se", "r22@nfi.se", "djiogwa@nfi.se", "jda82@nfi.se", "0182@nfi.se", "cnzjwaui@nfi.se" };

            // Search string
            string searchKerword = "jda82";


            // Loop emails
            foreach(string email in emails)
            {
                // Checking...
                Console.WriteLine("Comparing: " + email);

                // Compare email with search keyword
                if(email.Contains(searchKerword))
                {
                    // Found
                    Console.WriteLine("Email " + email + " found in the array! Breaking out...");
                    // Break out from loop since you've already found the email in question.
                    break;
                }
            }
            #endregion

            Console.WriteLine("-+-+-+-+-+-+-+-+-+-+-\n");
            
            #region Uppgift_3
            // Ai som går över en väg och kollar efter bilar.

            bool cars = true;

            Random randomGen = new Random();

            while (cars)
            {
                if(randomGen.Next(0, 5) > 0)
                {
                    cars = true;
                }
                else
                {
                    cars = false;
                }
                if(cars)
                {
                    Console.WriteLine("Det kommer bilar, Ain går över vägen.");
                }
                else
                {
                    Console.WriteLine("Inga bilar, Ain går inte över vägen.");
                }
            }

            #endregion

            Console.Write("\n\nTryck enter för att gå vidare till uppgift 8...");
            Console.ReadKey();

            // Övning 8:
            #region Övning8_Uppgift_1
            Console.Clear();

            string donationOutput(string namePerson, double amountMoney, bool returnable = false)
            {
                string combinedString = namePerson + " har donerat " + amountMoney + " kr!";
                if (returnable)
                {
                    return combinedString;
                }
                Console.WriteLine(combinedString);
                return "";
            }

            donationOutput("Christopher", 69.99);

            #endregion

            #region Övning8_Uppgift_2

            Console.WriteLine("Klicka enter för att rita ut ditt sänka skepp bräde...");
            Console.ReadKey();
            Console.Clear();
            Console.WriteLine("-+-+-+-+-+-+-+-+-+-+-\n");

            void sänkaBåtar(string[][] board)
            {
                foreach (string[] horizontal in board)
                {
                    foreach (string cell in horizontal)
                    {
                        Console.Write(cell + " ");
                    }
                    Console.WriteLine();
                }
            }

            string[][] mainBoard = new string[5][];
            for (int i = 0; i < 5; i++)
            {
                mainBoard[i] = new string[6];
                for (int j = 0; j < 6; j++)
                {
                    mainBoard[i][j] = "X";
                }
            }

            sänkaBåtar(mainBoard);


            #endregion


            Console.Write("\n\nTryck enter för att gå vidare till uppgift 9...");
            Console.ReadKey();

            // Övning 9:
            #region Övning9_Uppgift_1
            Console.Clear();

            double inCelcius = 14;

            double convertTemp(double celcius)
            {
                return ((celcius * 9 / 5) +32);
            }

            Console.WriteLine(inCelcius + " celcius i farenheit är " + convertTemp(inCelcius) + ".");
            Console.ReadKey();
            #endregion

            #region Övning9_Uppgift_2
            Console.Clear();

            string generateWordFromChar(char alphabethChar)
            {
                switch (char.ToUpper(alphabethChar))
                {
                    case 'A':
                        return "Adventure!";
                    case 'B':
                        return "Bongo";
                    case 'C':
                        return "Celcius!!!";
                    case 'D':
                        return "Duolingo.";
                    case 'E':
                        return "Epic";
                    case 'F':
                        return "Fantastic!";
                    case 'G':
                        return "Gigantic";
                    case 'H':
                        return "Harmony";
                    case 'I':
                        return "Incredible!";
                    case 'J':
                        return "Jubilation";
                    case 'K':
                        return "Kaleidoscope";
                    case 'L':
                        return "Luminous";
                    case 'M':
                        return "Majestic";
                    case 'N':
                        return "Nebula";
                    case 'O':
                        return "Opulent";
                    case 'P':
                        return "Panorama";
                    case 'Q':
                        return "Quasar";
                    case 'R':
                        return "Radiant";
                    case 'S':
                        return "Serendipity";
                    case 'T':
                        return "Tranquil";
                    default:
                        return "WOMP WOMP";
                }
            }

            Console.WriteLine("Input a Char for a nice word!");
            char userLetter = Console.ReadLine().ToString()[0];

            Console.WriteLine(userLetter + " --> " + generateWordFromChar(userLetter)); 

            #endregion

            Console.ReadKey();

        }
    }
}
