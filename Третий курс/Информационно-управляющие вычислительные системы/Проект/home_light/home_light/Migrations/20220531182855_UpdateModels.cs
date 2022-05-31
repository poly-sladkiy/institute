using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace home_light.Migrations
{
    public partial class UpdateModels : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Datas_Sensors_SensorId",
                table: "Datas");

            migrationBuilder.DropForeignKey(
                name: "FK_Flashlights_Sensors_SensorId",
                table: "Flashlights");

            migrationBuilder.DropForeignKey(
                name: "FK_Sensors_Rooms_RoomId",
                table: "Sensors");

            migrationBuilder.AlterColumn<int>(
                name: "RoomId",
                table: "Sensors",
                type: "integer",
                nullable: false,
                defaultValue: 0,
                oldClrType: typeof(int),
                oldType: "integer",
                oldNullable: true);

            migrationBuilder.AlterColumn<int>(
                name: "SensorId",
                table: "Flashlights",
                type: "integer",
                nullable: false,
                defaultValue: 0,
                oldClrType: typeof(int),
                oldType: "integer",
                oldNullable: true);

            migrationBuilder.AlterColumn<int>(
                name: "SensorId",
                table: "Datas",
                type: "integer",
                nullable: false,
                defaultValue: 0,
                oldClrType: typeof(int),
                oldType: "integer",
                oldNullable: true);

            migrationBuilder.AddForeignKey(
                name: "FK_Datas_Sensors_SensorId",
                table: "Datas",
                column: "SensorId",
                principalTable: "Sensors",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Flashlights_Sensors_SensorId",
                table: "Flashlights",
                column: "SensorId",
                principalTable: "Sensors",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_Sensors_Rooms_RoomId",
                table: "Sensors",
                column: "RoomId",
                principalTable: "Rooms",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Datas_Sensors_SensorId",
                table: "Datas");

            migrationBuilder.DropForeignKey(
                name: "FK_Flashlights_Sensors_SensorId",
                table: "Flashlights");

            migrationBuilder.DropForeignKey(
                name: "FK_Sensors_Rooms_RoomId",
                table: "Sensors");

            migrationBuilder.AlterColumn<int>(
                name: "RoomId",
                table: "Sensors",
                type: "integer",
                nullable: true,
                oldClrType: typeof(int),
                oldType: "integer");

            migrationBuilder.AlterColumn<int>(
                name: "SensorId",
                table: "Flashlights",
                type: "integer",
                nullable: true,
                oldClrType: typeof(int),
                oldType: "integer");

            migrationBuilder.AlterColumn<int>(
                name: "SensorId",
                table: "Datas",
                type: "integer",
                nullable: true,
                oldClrType: typeof(int),
                oldType: "integer");

            migrationBuilder.AddForeignKey(
                name: "FK_Datas_Sensors_SensorId",
                table: "Datas",
                column: "SensorId",
                principalTable: "Sensors",
                principalColumn: "Id");

            migrationBuilder.AddForeignKey(
                name: "FK_Flashlights_Sensors_SensorId",
                table: "Flashlights",
                column: "SensorId",
                principalTable: "Sensors",
                principalColumn: "Id");

            migrationBuilder.AddForeignKey(
                name: "FK_Sensors_Rooms_RoomId",
                table: "Sensors",
                column: "RoomId",
                principalTable: "Rooms",
                principalColumn: "Id");
        }
    }
}
