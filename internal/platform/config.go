package platform

import "fmt"

type Config struct {
	Version string
	Region  string
	Env     string
}

func LoadConfig() (*Config, error) {
	cfg := &Config{
		Version: "0.1.0",
		Region:  "us-east-1",
		Env:     "development",
	}

	if cfg.Version == "" {
		return nil, fmt.Errorf("invalid platform configuration")
	}

	return cfg, nil
}
