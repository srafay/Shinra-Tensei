using System;
using System.Collections.Generic;
using System.Linq;

namespace Blazor_Pizza.Models
{
    public class Pizza
    {
        public const int DefaultSize = 12;
        public const int MinimumSize = 9;
        public const int MaximumSize = 17;

        public int Id { get; set; }

        public int OrderId { get; set; }

        public PizzaSpecial Special { get; set; }

        public int SpecialId { get; set; }

        public int Size { get; set; }

        public List<PizzaTopping> Toppings { get; set; }

        public decimal GetBasePrice()
        {
            System.Console.WriteLine("Base Price returning {0}", ((decimal)Size / (decimal)DefaultSize) * Special.BasePrice);
            return ((decimal)Size / (decimal)DefaultSize) * Special.BasePrice;
        }

        public decimal GetTotalPrice()
        {
            // return GetBasePrice() + Toppings.Sum(t => t.Topping.Price);
            return GetBasePrice();
        }

        public string GetFormattedTotalPrice()
        {
            return GetTotalPrice().ToString("0.00");
        }
    }
}