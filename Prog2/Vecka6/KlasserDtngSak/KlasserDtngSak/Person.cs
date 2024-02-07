using System;


namespace KlasserDtngSak
{
    class Person
    {
        private string name;
        private string lname;
        private int age;
        private string personal_hobby;

        public Person(string name_constr, string lname_constr, int age_constr, string personal_hobby_constr)
        {
            name = name_constr;
            lname = lname_constr;
            age = age_constr;
            personal_hobby = personal_hobby_constr;
        }
        
        public void WhoAmI()
        {
            Console.WriteLine("My name is {0}, {1} {0}. And my hobby is {2}. (I'm also {3} years young)", lname, name, personal_hobby, age);
        }

    }
}
