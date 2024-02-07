using System;

namespace Bilpanel
{
    class Car
    {
        // L for liter.
        // Car model
        private string model;
        // Max fuel allowed in car. (In L)
        private double maxFuelL;
        // Current amount of fuel left.(In L)
        private double curFuelL;
        // Current burning per kilometer.
        private double curBurningPerKm = 0.9;

        public Car(string model_constr, double maxFuelL_constr)
        {
            model = model_constr;
            maxFuelL = maxFuelL_constr;
            curFuelL = maxFuelL_constr;
        }

        public string howMuchCanIFuelUpFor()
        {
            // Temporary var for saving the current amount you can fill the tank with until its full.
            double tempL = maxFuelL - curFuelL;
            if(tempL <= 0)
            {
                // Full tank
                return "Your tank is already full.";
            }
            else
            {
                return $"You can fill your tank with {tempL} L.";
            }
        }
        public void drive(int distance)
        {
            // Calculate fuel consumption for the given distance
            double fuelConsumed = distance * curBurningPerKm;

            if (fuelConsumed > curFuelL)
            {
                // Not enough fuel to cover the entire distance
                Console.WriteLine($"Not enough fuel to drive {distance} km. Refuel required.");
            }
            else
            {
                // Sufficient fuel, update the fuel level
                curFuelL -= fuelConsumed;
                Console.WriteLine($"Successfully drove {distance} km. Remaining fuel: {curFuelL} L");
            }
        }

        public void fuel(int amount)
        {
            double afterFueled = curFuelL + amount;
            if(afterFueled >= maxFuelL)
            {
                Console.WriteLine("You cannot fuel more than the tank holds.");
            }
            else
            {
                curFuelL = afterFueled;
                Console.WriteLine("You fueled up with {0} and you now have {1} L in your tank.", amount, afterFueled);
            }
        }

        public void howFarCanIDrive()
        {
            if (curFuelL <= 0)
            {
                Console.WriteLine("Your tank is empty. Refuel required.");
            }
            else
            {
                double maxDistance = curFuelL / curBurningPerKm;
                Console.WriteLine($"With the current fuel level, you can drive approximately {maxDistance} km.");
            }
        }

        public void summary()
        {
            Console.WriteLine($"Current fuel amount: {curFuelL}.");
            Console.WriteLine(howMuchCanIFuelUpFor());
            howFarCanIDrive();
        }
    }
}
