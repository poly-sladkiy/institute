using home_light.Extensions;
using Microsoft.OpenApi.Models;
using System.Reflection;

var builder = WebApplication.CreateBuilder(args);
#region builder
// Add services to the container.

builder.Services.AddCors(options => options.AddPolicy("CorsPolicy",
                            builder =>
                            {
                                builder.AllowAnyHeader()
                                       .AllowAnyMethod()
                                       .SetIsOriginAllowed((host) => true)
                                       .AllowCredentials();
                            }));

builder.Services.AddControllers();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo
    {
        Version = "v1",
        Title = "Home Light",
        Description = "ASP.NET Core Web API",
        Contact = new OpenApiContact
        {
            Name = "Ignakov Konstantin & Victor Tihonov",
            Email = string.Empty,
        },
        License = new OpenApiLicense
        {
            Name = "PLTH API",
        }
    });
    c.SchemaFilter<AddSchemaDefaultValues>();
    c.SchemaFilter<SwaggerSkipPropertyFilter>();
    c.DocumentFilter<SwaggerAddEnumDescriptions>();
    var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    var xmlPath = System.IO.Path.Combine(AppContext.BaseDirectory, xmlFile);
    c.IncludeXmlComments(xmlPath);
});

// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
#endregion
var app = builder.Build();
#region app
// Configure the HTTP request pipeline.
app.UseSwagger();
app.UseSwaggerUI();
app.UseCors("CorsPolicy");


//app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
#endregion
