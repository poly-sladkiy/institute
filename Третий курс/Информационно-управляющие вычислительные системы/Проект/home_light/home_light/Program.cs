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