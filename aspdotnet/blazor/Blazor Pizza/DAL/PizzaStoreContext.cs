using Microsoft.EntityFrameworkCore;
using Blazor_Pizza.Models;

namespace Blazor_Pizza.DAL
{
  public class PizzaStoreContext : DbContext
  {
    public PizzaStoreContext(
        DbContextOptions options) : base(options)
    {
    }

    public DbSet<PizzaSpecial> Specials { get; set; }
  }
}