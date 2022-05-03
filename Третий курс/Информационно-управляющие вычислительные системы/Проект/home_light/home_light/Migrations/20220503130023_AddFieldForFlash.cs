using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace home_light.Migrations
{
    public partial class AddFieldForFlash : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<bool>(
                name: "IsShining",
                table: "Flashlights",
                type: "boolean",
                nullable: false,
                defaultValue: false);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "IsShining",
                table: "Flashlights");
        }
    }
}
