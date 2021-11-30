using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Simple_Programs
{
    abstract class Person
    {
        public string Name;
        public int Age { get; set; }
        public string Address { get; set; }

        public Person(string name, int age, string address)
        {
            Name = name;
            Age = age;
            Address = address;
        }

        /* Abstract methods cannot have a implementation and child should implement them */
        public abstract int CalculateAge();

        /* Virtual methods should have definition and child COULD override them */
        public virtual int CalculateDOB()
        {
            return 0;
        }
    }

    class Employee<T, TSalary> : Person
    {
        public string CompanyName { get; set; }
        public T Points {get;set;}
        public TSalary Salary { get; set; }
        public string Designation { get; set; }

        public Employee(string name, int age, string address, string companyname, string designation, T points, TSalary salary) : base (name, age, address)
        {
            CompanyName = companyname;
            Designation = designation;
            Points = points;
            Salary = salary;

        }

        public override int CalculateAge()
        {
            return Age;
        }

        public override int CalculateDOB()
        {
            return base.CalculateDOB() + 1;
        }
    }


}
