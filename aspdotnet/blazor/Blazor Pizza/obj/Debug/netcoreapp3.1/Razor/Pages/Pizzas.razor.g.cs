#pragma checksum "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "c9610edcd919ef7c861844a44fb12f5e330483cc"
// <auto-generated/>
#pragma warning disable 1591
namespace Blazor_Pizza.Pages
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Components;
#nullable restore
#line 1 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using System.Net.Http;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using Microsoft.AspNetCore.Authorization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using Microsoft.AspNetCore.Components.Authorization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using Microsoft.AspNetCore.Components.Forms;

#line default
#line hidden
#nullable disable
#nullable restore
#line 5 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using Microsoft.AspNetCore.Components.Routing;

#line default
#line hidden
#nullable disable
#nullable restore
#line 6 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using Microsoft.AspNetCore.Components.Web;

#line default
#line hidden
#nullable disable
#nullable restore
#line 7 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using Microsoft.JSInterop;

#line default
#line hidden
#nullable disable
#nullable restore
#line 8 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using Blazor_Pizza;

#line default
#line hidden
#nullable disable
#nullable restore
#line 9 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\_Imports.razor"
using Blazor_Pizza.Shared;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
using Blazor_Pizza.Data;

#line default
#line hidden
#nullable disable
    [Microsoft.AspNetCore.Components.RouteAttribute("/pizzas")]
    public partial class Pizzas : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
            __builder.AddMarkupContent(0, "<h1>Choose your pizza</h1>\r\n\r\n");
            __builder.AddMarkupContent(1, "<p>We have all these delicious recipes:</p>\r\n\r\n");
#nullable restore
#line 10 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
 if (todaysPizzas == null)
{

#line default
#line hidden
#nullable disable
            __builder.AddContent(2, "    ");
            __builder.AddMarkupContent(3, "<p>We\'re finding out what pizzas are available today...</p>\r\n");
#nullable restore
#line 13 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
}
else
{

#line default
#line hidden
#nullable disable
            __builder.AddContent(4, "    ");
            __builder.OpenElement(5, "table");
            __builder.AddMarkupContent(6, "\r\n        ");
            __builder.AddMarkupContent(7, @"<thead>
            <tr>
                <th>Pizza Name</th>
                <th>Description</th>
                <th>Vegetarian?</th>
                <th>Vegan?</th>
                <th>Price</th>
            </tr>
        </thead>
        
        ");
            __builder.OpenElement(8, "tbody");
            __builder.AddMarkupContent(9, "\r\n");
#nullable restore
#line 28 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
             foreach (var pizza in todaysPizzas)
            {

#line default
#line hidden
#nullable disable
            __builder.AddContent(10, "                ");
            __builder.OpenElement(11, "tr");
            __builder.AddMarkupContent(12, "\r\n                    ");
            __builder.OpenElement(13, "td");
            __builder.AddContent(14, 
#nullable restore
#line 31 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
                         pizza.Name

#line default
#line hidden
#nullable disable
            );
            __builder.CloseElement();
            __builder.AddMarkupContent(15, "\r\n                    ");
            __builder.OpenElement(16, "td");
            __builder.AddContent(17, 
#nullable restore
#line 32 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
                         pizza.Description

#line default
#line hidden
#nullable disable
            );
            __builder.CloseElement();
            __builder.AddMarkupContent(18, "\r\n                    ");
            __builder.OpenElement(19, "td");
            __builder.AddContent(20, 
#nullable restore
#line 33 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
                         pizza.Vegetarian

#line default
#line hidden
#nullable disable
            );
            __builder.CloseElement();
            __builder.AddMarkupContent(21, "\r\n                    ");
            __builder.OpenElement(22, "td");
            __builder.AddContent(23, 
#nullable restore
#line 34 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
                         pizza.Vegan

#line default
#line hidden
#nullable disable
            );
            __builder.CloseElement();
            __builder.AddMarkupContent(24, "\r\n                    ");
            __builder.OpenElement(25, "td");
            __builder.AddContent(26, 
#nullable restore
#line 35 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
                         pizza.Price

#line default
#line hidden
#nullable disable
            );
            __builder.CloseElement();
            __builder.AddMarkupContent(27, "\r\n                ");
            __builder.CloseElement();
            __builder.AddMarkupContent(28, "\r\n");
#nullable restore
#line 37 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
            }

#line default
#line hidden
#nullable disable
            __builder.AddContent(29, "        ");
            __builder.CloseElement();
            __builder.AddMarkupContent(30, "\r\n    ");
            __builder.CloseElement();
            __builder.AddMarkupContent(31, "\r\n");
#nullable restore
#line 40 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
}

#line default
#line hidden
#nullable disable
        }
        #pragma warning restore 1998
#nullable restore
#line 43 "D:\Projects\Shinra-Tensei\aspdotnet\blazor\Blazor Pizza\Pages\Pizzas.razor"
 
    private Pizza[] todaysPizzas;

    protected override async Task OnInitializedAsync()
    {
       //todaysPizzas = await PizzaSvc.GetPizzasAsync();
    }

#line default
#line hidden
#nullable disable
        [global::Microsoft.AspNetCore.Components.InjectAttribute] private PizzaService PizzaSvc { get; set; }
    }
}
#pragma warning restore 1591
