using System;

namespace Simple_Programs
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Prime Program */
            /*IsPrime PrimeChecker = new();

            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 19, 23, 29, 31, 37, 41, 47, 48, 97, 999983, 999985, 1299709, 1299710, 2147483647 };
            for (int j = 0; j < numbers.Length; j++)
                Console.WriteLine(String.Format("{0} is prime [{1}]", numbers[j], PrimeChecker.CheckPrime(numbers[j])));*/
            /* Prime Program */

            /* Inheritance Program */
            Employee<int, string> employee = new Employee<int, string>("Syed", 25, "Australia", "CDU", "Software Engineer", 2,"100");
            Console.WriteLine(String.Format("Employee name: {0}", employee.Name));
            Console.WriteLine(String.Format("Employee age: {0}", employee.Age));
            Console.WriteLine(String.Format("Employee company: {0}", employee.CompanyName));
            Console.WriteLine(String.Format("Employee salary: {0}", employee.Salary));
            Console.WriteLine(String.Format("Employee points: {0}", employee.Points));
            /* Inheritance Program */
        }
    }
}
