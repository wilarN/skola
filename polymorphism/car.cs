using System;

namespace myClasses
{
    class animal
    {
        public virtual void sound()
        {
            Console.WriteLine("Generic animal sound.");
        }
    }

    class pig : animal
    {
        public override void sound()
        {
            Console.WriteLine("Oink oink.");
        }
    }
}
