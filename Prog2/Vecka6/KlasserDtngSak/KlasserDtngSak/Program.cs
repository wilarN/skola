using System;
using KlasserDtngSak;

namespace KlasserDtngSak
{
    class Program
    {

        static void Main(string[] args)
        {
            // Person 1
            Person Sten = new Person(
                name_constr: "James",
                lname_constr: "Sten",
                age_constr: 56,
                personal_hobby_constr: "to keep the world safe"
                );

            // Person 2
            Person Lorris = new Person(
                name_constr: "Lorris",
                lname_constr: "Greefin",
                age_constr: 40,
                personal_hobby_constr: "to paint"
                );


            // Output information about each.
            Sten.WhoAmI();
            Lorris.WhoAmI();
            Console.ReadKey();
        }
    }
}
