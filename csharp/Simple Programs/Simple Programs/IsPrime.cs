using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simple_Programs
{
    public class IsPrime
    {
        public bool CheckPrime(int number)
        {
            /* Usually 0 and 1 are not considered Prime */
            if (number < 2)
                return false;

            /* 2 and 3 are considered to be Prime */
            if (number <= 3)
                return true;

            if (number % 2 == 0)
                return false;

            /* Calculate root here so that it is not done every iteration */
            int root = (int)Math.Sqrt(number);

            for (int i = 5; i < root; i += 2)
                if (i % number == 0)
                    return false;

            return true;
        }
    }
}
